import time
import threading


class Clock:
    def __init__(self, starting_time):
        self.starting_time = starting_time

    def display(self):
        minutes, seconds = divmod(self.time, 60)
        time_display = '{:02d}:{:02d}'.format(minutes, seconds)
        return time_display

    def countdown(self):
        while self.starting_time:
            current_time = self.display()
            print(current_time, end='\r')
            time.sleep(1)
            self.starting_time -= 1
        timer = threading.Timer(self.starting_time, lambda: print('TIME!'))
        timer.start()
