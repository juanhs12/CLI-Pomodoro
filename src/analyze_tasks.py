import csv
import os

def format_duration(minutes):
    hours = minutes // 60
    remaining_minutes = minutes % 60
    if hours > 0:
        return f"{hours}h {remaining_minutes}m"
    return f"{remaining_minutes}m"

def analyze_task_percentages(file_path='pomodoros.csv'):
    if not os.path.exists(file_path):
        # If not found in current dir, check parent dir
        if os.path.exists('../pomodoros.csv'):
            file_path = '../pomodoros.csv'
        else:
            print("CSV file not found.")
            return

    task_durations = {}
    total_duration = 0

    with open(file_path, 'r', newline='') as file:
        reader = csv.reader(file)
        headers = next(reader, None) # Skip headers

        for row in reader:
            if not row or len(row) < 4:
                continue
            
            task_name = row[0]
            duration_str = row[3]
            
            # Extract numeric value from "X min"
            try:
                duration = int(duration_str.split()[0])
            except (ValueError, IndexError):
                continue

            task_durations[task_name] = task_durations.get(task_name, 0) + duration
            total_duration += duration

    if total_duration == 0:
        print("No task data found or total duration is zero.")
        return

    print("\nTask Time Distribution:")
    print("-" * 40)
    # Sort by duration descending
    sorted_tasks = sorted(task_durations.items(), key=lambda x: x[1], reverse=True)
    
    for task_name, duration in sorted_tasks:
        percentage = (duration / total_duration) * 100
        formatted_time = format_duration(duration)
        print(f"{task_name:.<25} {percentage:>6.2f}% ({formatted_time})")
    
    print("-" * 40)
    print(f"Total time: {format_duration(total_duration)} ({total_duration} min)")

if __name__ == "__main__":
    analyze_task_percentages()
