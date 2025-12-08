import time

alarm_time = input("Enter alarm time (HH:MM:SS): ")

print("Alarm set for", alarm_time)

while True:
    now = time.strftime("%H:%M:%S")
    if now == alarm_time:
        print("\nALARM! Time's up!")
        break
    time.sleep(1)
