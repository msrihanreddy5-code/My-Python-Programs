import threading, requests

def fetch(url):
    print(len(requests.get(url).text))

urls = ["https://example.com"]*5
for u in urls:
    threading.Thread(target=fetch, args=(u,)).start()
