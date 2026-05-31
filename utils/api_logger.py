import allure
import json


def log_api_response(response):
    with allure.step("API Call Details"):

        # Request info
        allure.attach(
            f"{response.request.method} {response.request.url}",
            name="Request",
            attachment_type=allure.attachment_type.TEXT
        )

        # Status code
        allure.attach(
            str(response.status_code),
            name="Status Code",
            attachment_type=allure.attachment_type.TEXT
        )

        # Response body (safe handling for JSONPlaceholder)
        try:
            body = response.json()
            formatted_body = json.dumps(body, indent=2)
        except Exception:
            formatted_body = response.text

        allure.attach(
            formatted_body,
            name="Response Body",
            attachment_type=allure.attachment_type.JSON
        )