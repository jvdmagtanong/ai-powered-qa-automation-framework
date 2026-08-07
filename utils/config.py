import os
from dotenv import load_dotenv

load_dotenv()

BASE_UI_URL=os.getenv("BASE_UI_URL")
BASE_API_URL=os.getenv("BASE_API_URL")
USERNAME=os.getenv("USERNAME")
PASSWORD=os.getenv("PASSWORD")
HEADED=os.getenv("HEADED", "False").lower() == "true"

if not BASE_API_URL or not BASE_UI_URL:
    raise ValueError("Missing required environment variables")
