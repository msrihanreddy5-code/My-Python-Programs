from cryptography.fernet import Fernet

key = Fernet.generate_key()
f = Fernet(key)

data = f.encrypt(b"Secret Data")
print(f.decrypt(data))
