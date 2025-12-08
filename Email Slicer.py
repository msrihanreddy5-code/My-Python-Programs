email = input("Enter your email: ")

username = email.split("@")[0]
domain = email.split("@")[1]

print("Username:", username)
print("Domain:", domain)
