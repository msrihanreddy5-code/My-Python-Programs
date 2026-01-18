import queue, threading

tasks = queue.Queue()

def worker():
    while True:
        print("Processing:", tasks.get())

threading.Thread(target=worker, daemon=True).start()
tasks.put("Task-1")
tasks.put("Task-2")
