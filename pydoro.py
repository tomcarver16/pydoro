import time
import sys    
import datetime
import argparse
import os

#Constants
CURSOR_UP_ONE = '\x1b[1A'
ERASE_LINE = '\x1b[2K'


class Timer:
    def __init__(self, seconds, timeType):
        self.seconds = seconds
        self.time = seconds
        self.timeType = timeType
        try:
            for i in range(0, seconds):
                self.i = i
                self.time = self.tick()
                self.show_time(self.time)
                time.sleep(1)
        except KeyboardInterrupt:
            self.validate_quit()

    def validate_quit(self):
        sys.stdout.write(ERASE_LINE + '\b\b')
        action = str(raw_input("Do you want to quit Y/N: ")).lower()
        if action == 'y':
            sys.exit()
        elif action == 'n':
            focusMins = int(input("How many focus mins do you want: "))
            breakMins = int(input("How many break mins do you want: "))
            create_timers(focusMins, breakMins)

    def tick(self):
        return self.time - 1

    def progress(self, count, total, suffix=''):
        bar_len = 60
        filled_len = int(round(bar_len * count / float(total)))

        percents = round(100.0 * count / float(total), 1)
        bar = '=' * filled_len + '-' * (bar_len - filled_len)

        sys.stdout.write('[%s] %s%s %s\r' % (bar, percents, '%', suffix))
        sys.stdout.flush() 

    def show_time(self, time):
        x = str(datetime.timedelta(seconds=time))
        sys.stdout.write("\r{0} Timer: {1}".format(self.timeType, x))
        self.progress(self.i, self.seconds, suffix='Complete')
        sys.stdout.flush()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--focus_time', help='Focus minutes', type=int, default=25)
    parser.add_argument('-b', '--break_time', help='Break minutes', type=int, default=5)
    args = parser.parse_args()
    create_timers(args.focus_time, args.break_time)
    # isBackground = parser.add_argument('--background', help='If the timer is running in the background', type=bool, default=False)

def print_clock():
    clock = """
.'`~~~~~~~~~~~`'.
(  .'11 12 1'.  )
|  :10 \|   2:  |
|  :9   @   3:  |
|  :8       4;  |
'. '..7 6 5..' .'
 ~-------------~ 
    """
    sys.stdout.write(clock)
    return

def create_timers(focusMins, breakMins):
    focusTime = True
    try:
        while focusTime == True:
            focusTimer = Timer(focusMins*60, "Focus")
            print_clock()
            focusTime = False
        else:
            breakTimer = Timer(breakMins*60, "Break")
            print_clock()
            focusTime = True
    except KeyboardInterrupt as ki:
        sys.exit()
        
def clear_screen():
    if os.name == "posix":
        os.system("clear")
    elif os.name == "nt":
        os.system("cls")
    return

if __name__ == "__main__":
    clear_screen()
    main()