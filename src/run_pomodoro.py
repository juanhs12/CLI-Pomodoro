import time
import os
import chime
import sys

YELLOW = '\033[33m'
GREEN = '\033[32m'
RED = '\033[31m'
RESET = '\033[0m'
class Timer:
    def run_flowmodoro(self, max_minutes):
        print("Flowmodoro iniciado. Pressione Ctrl+C para pausar.")
        os.system('tput bel')
        time.sleep(1)
        os.system('tput bel')
        time.sleep(1)
        os.system('tput bel')
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
                    print(f"\r{max_minutes}m\r{GREEN}{current_total // 60}m {current_total % 60}s{RESET}", end="", flush=True)
                    time.sleep(1)
                
                print("\nTempo máximo atingido!")
                total_work_done += work_done_in_block
                self._do_break(work_done_in_block)
                
            except KeyboardInterrupt:
                try:
                    print(f"\nFluxo pausado aos {work_done_in_block // 60}m {work_done_in_block % 60}s.")
                    total_work_done += work_done_in_block
                    if not self._do_break(work_done_in_block):
                        print("\rSalvando\r")
                        time.sleep(2)
                        return True
                        #raise SystemExit("\nSaindo sem salva.")
                    if total_work_done < total_goal_seconds:
                        print(f"\nRetomando fluxo. Total trabalhado: {total_work_done // 60}m {total_work_done % 60}s / {max_minutes}m.")

                except KeyboardInterrupt: 
                    return True
                    #raise SystemExit("\nSaindo sem salva.")

    def _do_break(self, work_done_seconds):
        break_time = int(work_done_seconds * 0.20)
        print(f"\n{YELLOW}Iniciando pausa de {break_time // 60}m {break_time % 60}s. {RESET}(Ctrl+C para cancelar e sair)")
        os.system('tput bel')
        time.sleep(1)
        os.system('tput bel')
        time.sleep(1)
        os.system('tput bel')
        chime.theme('zelda')
        chime.success()
        try:
            self.countdown(break_time, mode='break')
            print("\nPausa finalizada.")
            os.system('tput bel')
            time.sleep(1)
            os.system('tput bel')
            time.sleep(1)
            os.system('tput bel')
            chime.theme('sonic')
            chime.success()
            return True
        except KeyboardInterrupt:
            print("\nPausa cancelada.")
            return False

    def run_pomodoro(self, cycle_length, work_time, short_break, long_break):
        for i in range(cycle_length):
            print("\rWork timer started for", work_time, "minutes")
            os.system('tput bel')
            time.sleep(1)
            os.system('tput bel')
            time.sleep(1)
            os.system('tput bel')
            chime.theme('pokemon')
            chime.success()
            self.countdown(work_time * 60, mode='work')

            if i < cycle_length - 1:
                print("\nShort break timer started for", short_break, "minutes")
                os.system('tput bel')
                time.sleep(1)
                os.system('tput bel')
                time.sleep(1)
                os.system('tput bel')
                chime.theme('zelda')
                chime.success()
                self.countdown(short_break * 60, mode='break')
        if long_break > 0:
            print("\rLong break timer started for", long_break, "minutes")
            os.system('tput bel')
            time.sleep(1)
            os.system('tput bel')
            time.sleep(1)
            os.system('tput bel')
            chime.theme('sonic')
            chime.success()
            self.countdown(long_break * 60, mode='break') 
            print("\rLong break finish",)
            os.system('tput bel')
            time.sleep(1)
            os.system('tput bel')
            time.sleep(1)
            os.system('tput bel')
            chime.theme('material')
            chime.success()
        else: 
            os.system('tput bel')
            time.sleep(1)
            os.system('tput bel')
            time.sleep(1)
            os.system('tput bel')
            chime.theme('material')
            chime.success()


    def countdown(self, t, mode='work'):
        """
        work is GREEN, break is YELLOW
        """
        if mode == 'work':
            color = GREEN 
        elif mode == 'break':
            color = YELLOW
        else:
            color = RESET
        try:
            while t:
                mins, secs = divmod(t, 60)
                print("\r{}{:02d}:{:02d}{}".format(color,mins, secs,RESET), end="", flush=True)
                time.sleep(1)
                t -= 1
        except KeyboardInterrupt:
                print(f'\r{RED}Interrompido.{RESET})')
