import os
from dotenv import load_dotenv

class Config:
    def __init__(self):
        # Load environment variables from a .env file, if present
        load_dotenv()

    @property
    def cloud_storage_path(self):
        return os.getenv('CLOUD_STORAGE_PATH', 'path/to/default/storage')

    # Add more configuration properties as needed
