import os
import csv


def write_to_csv(task_name, pomodoro):
    # CSV file headers
    headers = ['Task Name', 'Start Time', 'End Time', 'Duration']
    # check for CSV file existence
    file_exists = os.path.isfile('pomodoros.csv')
    # now write the pomodoro to CSV file
    with open('pomodoros.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        # ff file doesnt already exist (first pomodoro), write headers first
        if not file_exists:
            writer.writerow(headers)
        
        start = pomodoro.get('start_time', 'N/A')
        end = pomodoro.get('end_time', 'N/A')
        duration = pomodoro.get('duration', 0)
        
        # write Pomodoro data to CSV
        writer.writerow([task_name, start, end, f"{duration} min"])
