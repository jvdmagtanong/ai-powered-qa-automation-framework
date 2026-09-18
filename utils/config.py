import os
from dotenv import load_dotenv


load_dotenv()


def get_required_env(name: str) -> str:
    value = os.getenv(name)

    if not value:
        raise ValueError(f"Missing required environment variable: {name}")

    return value


BASE_UI_URL = get_required_env("BASE_UI_URL")
BASE_API_URL = get_required_env("BASE_API_URL")
USERNAME = get_required_env("USERNAME")
PROBLEM_USERNAME = get_required_env("PROBLEM_USERNAME")
PASSWORD = get_required_env("PASSWORD")
GEMINI_API_KEY = get_required_env("GEMINI_API_KEY")

HEADED = os.getenv("HEADED", "False").lower() == "true"