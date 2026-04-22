import sys, select, tty, termios

def is_key_pressed():
    old_settings = termios.tcgetattr(sys.stdin)
    try:
        tty.setraw(sys.stdin.fileno())
        select_in, _, _ = select.select([sys.stdin], [], [], 0)
        if select_in:
            return sys.stdin.read(1)
        return None
    finally:
        termios.tcsetattr(sys.stdin, termios.TCSADRAIN, old_settings)
