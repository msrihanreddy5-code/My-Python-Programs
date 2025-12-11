import time
frames = ["[]", "[ ]", "[  ]", "[ ]", "[]"]

while True:
    for f in frames:
        print(f"\r{f}", end="")
        time.sleep(0.2)
