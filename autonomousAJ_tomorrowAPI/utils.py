# autonomousAJ_tomorrowAPI/autonomousAJ_tomorrowAPI/utils.py
import os
import datetime
import pandas as pd
import xlsxwriter
from autonomousAJ_tomorrowAPI import config

base_path = config.BASE_PATH
class Script_Run_Logs:
    def __init__(self, script):
        self.script = script

    def script_start_log(self):
        print("-----------------------------------------------------")
        print(f"Script: {self.script}")
        print(f"Start Time: {datetime.datetime.now()}")

    def script_end_log(self):
        print(f"End Time: {datetime.datetime.now()}")
        print("-----------------------------------------------------")

class DF_Processor:
    def __init__(self, file_name):
        self.df = pd.read_csv(f"{base_path}/data_files/{file_name}.csv", low_memory=False)
        self.df.drop_duplicates(inplace=True)

    def fill_na(self, col_name, fill_value):
        self.df[col_name] = self.df[col_name].fillna(fill_value)

    def set_column_dtypes(self, col_dtype_dict):
        if not isinstance(col_dtype_dict, dict):
            raise TypeError("Expected a dictionary, got: {}".format(type(col_dtype_dict)))

        for col, dtype in col_dtype_dict.items():
            self.df[col] = self.df[col].astype(dtype)

    def df_col_list(self):
        return self.df.columns.tolist()

    def rename_columns(self, original_name, revised_name):
        self.df = self.df.rename(columns={original_name: revised_name})

    def write_to_csv(self, path):
        self.df.to_csv(path, index=False)

