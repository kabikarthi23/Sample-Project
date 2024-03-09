#Creating a python program on Countdown

#importing requiring libraries
import time

#creating the function
def CountDown(time_sec):
    while time_sec:
        min,sec = divmod(time_sec,60)
        timecount = "{:02d} : {:02d}".format(min,sec)
        print(timecount)
        time.sleep(1)
        time_sec -= 1

    print("Let's Start")

#calling the function
CountDown(10)