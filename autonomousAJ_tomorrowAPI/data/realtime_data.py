# autonomousAJ_tomorrowAPI/data/realtime_data.py
import pandas as pd
from autonomousAJ_tomorrowAPI.api.realtime import Realtime
from autonomousAJ_tomorrowAPI.config import global_config

class Realtime_Data:
    def __init__(self, location, location_name):
        self.location = location
        self.location_name = location_name
        self.tomorrow_realtime = Realtime()

    def get_and_process_realtime_data(self):
        data = self.tomorrow_realtime.get_realtime(self.location)
        if data:
            df = pd.DataFrame([data])
            df = df.join(df.pop('values').apply(pd.Series))
            self.save_realtime_data(df)

    def save_realtime_data(self, df):
        df.to_csv(f"{global_config.BASE_PATH}/data_files/written_files/realtime_data/realtime_{self.location_name}.csv", index=False)
        print(df)