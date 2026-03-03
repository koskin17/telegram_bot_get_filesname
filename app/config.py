import os
from dotenv import load_dotenv

load_dotenv()

class Config():
    API_ID = int(os.getenv("API_ID"))
    API_HASH = os.getenv("API_HASH")

    if not API_ID or not API_HASH:
        raise ValueError("API_ID or API_HASH not found in environment variables.")