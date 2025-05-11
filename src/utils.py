import threading

def set_interval(func,time):
    e = threading.Event()
    while not e.wait(time):
        func()