# autonomousAJ_tomorrowAPI/api/realtime.py
import datetime as dt
import pytz
import requests
import pandas as pd
from .base import Tomorrow_API_Base

class Realtime(Tomorrow_API_Base):
    def get_realtime(self, location):
        api_key = self.get_tomorrow_client()

        url = f"https://api.tomorrow.io/v4/weather/realtime?location={location}&apikey={api_key}"
        
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()['data']
            return data
        else:
            print("Error:", response.status_code, response.text)
            return None


