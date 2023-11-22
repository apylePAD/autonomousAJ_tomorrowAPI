# autonomousAJ_tomorrowAPI/autonomousAJ_tomorrowAPI/auth.py
import os
from dotenv import load_dotenv

load_dotenv()

class Get_Tomorrow_Client:
    def __init__(self):
        self.api_key = os.getenv('TOMORROW_API_KEY')

    def get_tomorrow_client(self):
        api_key = self.api_key
        return api_key

tomorrow_client = Get_Tomorrow_Client()