# autonomousAJ_tomorrowAPI/data/temperature_data.py
import pandas as pd
from autonomousAJ_tomorrowAPI.api.temperature import Temperature
from autonomousAJ_tomorrowAPI.config import global_config

class Temperature_Data:
    def __init__(self, location, location_name):
        self.location = location
        self.location_name = location_name
        self.tomorrow_temperatures = Temperature()

    def get_and_process_temperature_data(self):
        minutes = self.tomorrow_temperatures.get_temperature(self.location)
        df = pd.DataFrame(minutes)

        df = df.join(df.pop('values').apply(pd.Series))
        self.save_temperature_data(df)

    def save_temperature_data(self, df):
        df.to_csv(f"{global_config.BASE_PATH}/data_files/written_files/temperature_data/temperature_{self.location_name}.csv", index=False)
        print(df)

