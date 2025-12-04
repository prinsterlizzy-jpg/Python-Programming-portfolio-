import time

def schedule_task(func, seconds):
    while True:
        func()
        time.sleep(seconds)

# Example
def hello():
    print("Running task...")

schedule_task(hello, 5)
