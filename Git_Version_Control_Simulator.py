import hashlib

def commit(data):
    return hashlib.sha1(data.encode()).hexdigest()

print("Commit hash:", commit("Initial commit"))
