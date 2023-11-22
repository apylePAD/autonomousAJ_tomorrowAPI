# autonomousAJ_tomorrowAPI/api/temperature.py
import datetime as dt
import pytz
import requests
import pandas as pd
from .base import Tomorrow_API_Base

class Temperature(Tomorrow_API_Base):
    def get_temperature(self, location):
        api_key = self.get_tomorrow_client()

        url = f"https://api.tomorrow.io/v4/weather/forecast?location={location}&apikey={api_key}&units=imperial&fields=temperature"
        
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            minutes = data['timelines']['minutely']
            print(minutes)
            return minutes
        else:
            print("Error:", response.status_code, response.text)
            return None
        
        

 