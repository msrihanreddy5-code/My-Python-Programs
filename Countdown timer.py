import time

seconds = int(input("Enter seconds: "))

for i in range(seconds, -1, -1):
    print(i, end="\r")
    time.sleep(1)

print("Time's up!")
