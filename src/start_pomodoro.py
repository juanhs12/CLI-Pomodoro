from pomodoro_length import Pomodoro
import datetime
from run_pomodoro import Timer
from write_to_csv import write_to_csv
from analyze_tasks import analyze_task_percentages

class StartPomodoro:

    def __init__(self):
        self.pomodoros = [] 
        self.tasks = [] 
    
    def start(self):
        pomodoro_instance = Pomodoro()
        timer = Timer()

        mode = input('Choose mode: [p]omodoro, [f]lowmodoro or [a]nalyze: ').lower()
        
        if mode == 'a':
            analyze_task_percentages()
            return
        
        while True:
            task_name = input('Enter the name of the task this session is for: ')
            if task_name:
                break
            else:
                print("You must enter a task name. Please try again.")

        if mode == 'f':
            max_mins = int(input("Enter max minutes for this flowmodoro: "))
            start_time = datetime.datetime.now().replace(microsecond=0)
            try:
                timer.run_flowmodoro(max_mins)
            except SystemExit as e:
                print(e)
                return
            end_time = datetime.datetime.now().replace(microsecond=0)
            write_to_csv(task_name, {
                'duration': max_mins, 
                'task': task_name, 
                'start_time': start_time, 
                'end_time': end_time
            })
            return

        try:
            cycle_length, work_time, short_break, long_break = pomodoro_instance.user_preferences()  

            pomodoro = {
                'start_time': datetime.datetime.now().replace(microsecond=0),
                'end_time': datetime.datetime.now().replace(microsecond=0) + datetime.timedelta(minutes=work_time),
                'duration': work_time,
                'task': task_name,
            }
            self.pomodoros.append(pomodoro)

            task_exists = False
            for task in self.tasks:
                if task['name'] == task_name:
                    task['pomodoros'].append(pomodoro)
                    task_exists = True
                    break

            if not task_exists:
                task = {
                    'name': task_name,
                    'pomodoros': [pomodoro],
                }
                self.tasks.append(task)
            

            timer.run_pomodoro(cycle_length, work_time, short_break, long_break)

            write_to_csv(task_name, pomodoro)
        except KeyboardInterrupt:
            print("\nInterrupted. Writing current session to file...")
           # write_to_csv(task_name, {'duration': 0, 'task': task_name, 'start_time': 'N/A', 'end_time': 'N/A'})
