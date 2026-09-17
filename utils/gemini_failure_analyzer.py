from google import genai
from utils.config import GEMINI_API_KEY
from models.failure_context import FailureContext

def analyze_test_failure(context: FailureContext):
    """
    Sends a test failure stack trace to Gemini to get an automated root-cause analysis.
    """

    client = genai.Client(api_key=GEMINI_API_KEY)
    
    # Construct a structured prompt for the model
    prompt = f"""
    Analyze the following automated mobile test failure. Use the functional test
    context and technical evidence together. Do not assume that every failure is
    a test automation problem or an application defect. Base your conclusion on
    the evidence provided and clearly identify uncertainty when the evidence is
    insufficient.

    Test Name:
    {context.test_name}

    Epic:
    {context.epic or "Not provided"}

    Feature:
    {context.feature or "Not provided"}

    Test Story:
    {context.story or "Not provided"}

    Test Description:
    {context.description or "Not provided"}

    Failure / Stack Trace:
    {context.stack_trace or "Not provided"}
    """
    
    if context.page_source:
        prompt += f"\nSanitized HTML Snippet / Page Source at time of failure:\n{context.page_source[:2000]}" # Limit size
        
    prompt += """

    Classify the most likely cause using one of these categories:

    1. Application defect
    2. Automation/test defect
    3. Locator problem
    4. Flaky Test
    5. Timing/synchronization issue
    6. Environment
    7. Insufficient evidence

    An assertion failure alone does not establish an application defect.

    Do not classify a failure as a locator problem merely because an element
    was not found. Use the test context, page source, and failure evidence to
    determine whether the expected element should have been present.

    Provide your analysis in exactly this structure:

    **Root Cause Summary**
    A concise explanation of what most likely caused the failure.
    Use the test story and description to explain what functional behavior was expected, 
    then use the technical evidence to explain how the observed behavior caused the failure. 
    When the evidence supports a specific explanation of what the application did instead, 
    include that explanation rather than only describing the missing element.

    **Failure Classification**
    Choose one category from the list above and explain why. Don't include the number.

    **Evidence**
    List the specific evidence from the test description, stack trace,
    page source, or environment that supports the classification.

    **Recommended Fix**
    Give a practical recommendation. If a code change is appropriate,
    include a small relevant code example. Do not recommend changing the
    test merely to make it pass unless the evidence indicates the test is
    incorrect.

    **Confidence Level**
    State High, Medium, or Low and explain what additional evidence would
    increase confidence if necessary.
"""

    try:
        # Using gemini-2.5-flash as it is fast, highly capable, and has a great free tier
        response = client.models.generate_content(
            model='gemini-2.5-flash',
            contents=prompt,
        )
        return response.text
    except Exception as e:
        return f"Failed to generate analysis from Gemini: {str(e)}"