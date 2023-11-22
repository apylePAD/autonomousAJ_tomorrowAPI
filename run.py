# autonomousAJ_tomorrowAPI/run.py
import inquirer
from autonomousAJ_tomorrowAPI.data.realtime_data import Realtime_Data
from autonomousAJ_tomorrowAPI.data.temperature_data import Temperature_Data

def main_menu():
    questions = [
        inquirer.List('choice',
                      message="What type of data would you like to interact with?",
                      choices=['Realtime', 'Temperature', 'Exit']),
    ]
    return inquirer.prompt(questions)['choice']

def get_realtime_input():
    location = '38.9822,-94.6708'
    location_name = 'overlandPark_ks'
    realtime_processor = Realtime_Data(location, location_name)
    realtime_processor.get_and_process_realtime_data()

def get_temperature_input():
    location = '38.9822,-94.6708'
    location_name = 'overlandPark_ks'
    temperature_processor = Temperature_Data(location, location_name)
    temperature_processor.get_and_process_temperature_data()


def run():
    while True:
        choice = main_menu()
        if choice == 'Realtime':
            get_realtime_input()
        elif choice == 'Temperature':
            get_temperature_input()
        elif choice == 'Exit':
            break

if __name__ == '__main__':
    run()