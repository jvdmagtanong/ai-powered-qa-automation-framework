import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def analyze_failure(test_name, error_message):
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {
                    "role": "system",
                    "content": (
                        "You are a QA automation expert. "
                        "Analyze test failures and provide clear root cause analysis "
                        "and possible fixes."
                    )
                },
                {
                    "role": "user",
                    "content": f"""
                        Test Name: {test_name}

                        Failure:
                        {error_message}

                        Explain:
                        1. Likely root cause
                        2. What might be wrong in the test or application
                        3. Suggested fix
                        """
                }
            ],
            temperature=0.2
        )

        return response.choices[0].message.content

    except Exception as e:
        return f"AI analysis failed: {str(e)}"