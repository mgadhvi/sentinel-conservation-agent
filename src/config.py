import os
from dotenv import load_dotenv

# Load the .env file
load_dotenv()

# Geospatial Settings
DEFAULT_LAT = -3.4653
DEFAULT_LON = -62.2159
CLOUD_THRESHOLD = 10.0

# AI Settings
HF_TOKEN = os.getenv("HUGGINGFACEHUB_API_TOKEN")
MODEL_ID = "HuggingFaceH4/zephyr-7b-beta"

if not HF_TOKEN:
    raise ValueError("❌ HUGGINGFACEHUB_API_TOKEN not found in .env file!")