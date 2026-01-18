permissions = {"read":4, "write":2, "execute":1}

def check(p):
    return sum(permissions[x] for x in p)

print(check(["read","write"]))  # 6
