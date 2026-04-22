import time
import os
import chime
import sys

class Timer:
    def run_flowmodoro(self, max_minutes):
        print("Flowmodoro iniciado. Pressione Ctrl+C para pausar.")
        chime.theme('pokemon')
        chime.success()
        
        total_goal_seconds = max_minutes * 60
        total_work_done = 0
        
        while total_work_done < total_goal_seconds:
            start_time = time.time()
            work_done_in_block = 0
            try:
                while total_work_done + work_done_in_block < total_goal_seconds:
                    work_done_in_block = int(time.time() - start_time)
                    current_total = total_work_done + work_done_in_block
                    print(f"\rTempo decorrido: {current_total // 60}m {current_total % 60}s / {max_minutes}m (Ctrl+C para pausar)", end="", flush=True)
                    time.sleep(1)
                
                print("\nTempo máximo atingido!")
                total_work_done += work_done_in_block
                self._do_break(work_done_in_block)
                
            except KeyboardInterrupt:
                print(f"\nFluxo pausado aos {work_done_in_block // 60}m {work_done_in_block % 60}s.")
                total_work_done += work_done_in_block
                self._do_break(work_done_in_block)
                if total_work_done < total_goal_seconds:
                    print(f"\nRetomando fluxo. Total trabalhado: {total_work_done // 60}m {total_work_done % 60}s / {max_minutes}m.")

    def _do_break(self, work_done_seconds):
        break_time = int(work_done_seconds * 0.20)
        print(f"\nIniciando pausa de {break_time // 60}m {break_time % 60}s.")
        chime.theme('zelda')
        chime.success()
        self.countdown(break_time)
        print("\nPausa finalizada.")
        chime.theme('sonic')
        chime.success()

    def run_pomodoro(self, cycle_length, work_time, short_break, long_break):
        for i in range(cycle_length):
            print("Work timer started for", work_time, "minutes")
            chime.theme('pokemon')
            chime.success()
            self.countdown(work_time * 60)

            if i < cycle_length - 1:
                print("\nShort break timer started for", short_break, "minutes")
                chime.theme('zelda')
                chime.success()
                self.countdown(short_break * 60)

        print("\nLong break timer started for", long_break, "minutes")
        chime.theme('sonic')
        chime.success()
        self.countdown(long_break * 60)

    def countdown(self, t):
        try:
            while t:
                mins, secs = divmod(t, 60)
                # Sintaxe corrigida para evitar erro de f-string
                print("\r{:02d}:{:02d}".format(mins, secs), end="", flush=True)
                time.sleep(1)
                t -= 1
        except KeyboardInterrupt:
            print("\nCronômetro interrompido.")
