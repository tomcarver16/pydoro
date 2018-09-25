import time
import sys    
import datetime

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
            print()
            stored_exception=sys.exc_info()

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

if __name__ == "__main__":
    focusTime = True
    focusMins = int(input("How many focus mins do you want: "))
    breakMins = int(input("How many break mins do you want: "))
    while True:
        try:
            if focusTime == True:
                focusTimer = Timer(focusMins*60, "Focus")
                focusTime = False
            else:
                breakTimer = Timer(breakMins*60, "Break")
                focusTime = True
        except KeyboardInterrupt:
            break