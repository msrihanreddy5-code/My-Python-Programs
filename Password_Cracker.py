import itertools,string

password = "ab1"
for p in itertools.product(string.ascii_lowercase+string.digits, repeat=3):
    if "".join(p)==password:
        print("Cracked:", password)
        break
