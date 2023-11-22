# autonomousAJ_tomorrowAPI/api/base.py
from autonomousAJ_tomorrowAPI.auth import tomorrow_client
import requests

class Tomorrow_API_Base:
    def get_tomorrow_client(self):
        return tomorrow_client.get_tomorrow_client()
    
    def handle_api_call(self, api_function, *args, **kwargs):
        try:
            response = api_function(*args, **kwargs)
            response.raise_for_status()  # Raises an HTTPError for bad requests
            return response

        except requests.exceptions.HTTPError as errh:
            print(f"Http Error: {errh}")

        except requests.exceptions.ConnectionError as errc:
            print(f"Error Connecting: {errc}")

        except requests.exceptions.Timeout as errt:
            print(f"Timeout Error: {errt}")

        except requests.exceptions.RequestException as err:
            print(f"Other Error: {err}")

        return None