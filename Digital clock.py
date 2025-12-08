import time

while True:
    current_time = time.strftime("%H:%M:%S")
    print(current_time, end="\r")   # Updates in the same line
    time.sleep(1)
