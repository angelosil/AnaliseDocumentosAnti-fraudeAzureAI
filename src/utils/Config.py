import os
from dotenv import load_dotenv
load_dotenv()

class Config:
    CONTAINER_NAME = os.getenv("CONTAINER_NAME")
    STORAGE_CONNECTION_STRING = os.getenv("AZURE_STORAGE_CONNECTION_STRING")
    STORAGE_API_KEY = os.getenv("STORAGE_API_KEY")

    DOC_NAME = os.getenv("DOC_NAME")
    DOC_CONNECTION_STRING = os.getenv("DOC_CONNECTION_STRING")
    DOC_API_KEY =  os.getenv("DOC_API_KEY")    