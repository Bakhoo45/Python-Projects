#Countdown Timer

import time

my_time = int(input("Enter the time in seconds for the countdown: "))

for i in range(my_time, 0, -1):
    seconds = i % 60
    minutes = (i // 60) % 60
    hours = i // 3600
    print(f"{hours:02}:{minutes:02}:{seconds:02}")
    time.sleep(1)