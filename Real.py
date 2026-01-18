import time

with open("log.txt") as f:
    f.seek(0,2)
    while True:
        line = f.readline()
        if line:
            print("LOG:", line.strip())
        time.sleep(1)
