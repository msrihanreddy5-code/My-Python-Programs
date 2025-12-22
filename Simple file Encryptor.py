import os
import sys
import time
import random

def save_key(key_value):
    with open("xor_key.txt", "w") as key_file:
        key_file.write(str(key_value))
    print(f"[+] Encryption key saved as 'xor_key.txt'")

def load_key():
    if not os.path.exists("xor_key.txt"):
        print("[-] No key file found! Please generate one first.")
        return None

    try:
        with open("xor_key.txt", "r") as key_file:
            key_value = int(key_file.read().strip())
            if 1 <= key_value <= 255:
                return key_value
            else:
                print("[-] Invalid key found in file.")
                return None
    except Exception as e:
        print(f"[-] Error reading key: {e}")
        return None

def generate_key():
    key_value = random.randint(1, 255)
    save_key(key_value)
    print(f"[+] New key generated successfully! (Key: {key_value})")

def process_file(filename, key_value, mode="encrypt"):
    if not os.path.exists(filename):
        print("[-] File not found. Please check the file name.")
        return

    if mode == "encrypt":
        output_file = filename + ".enc"
    else:
        output_file = filename[:-4] + "_decrypted.txt" if filename.endswith(".enc") else filename + "_decrypted.txt"

    try:
        with open(filename, "rb") as infile:
            data = infile.read()

        processed_data = bytes([byte ^ key_value for byte in data])

        with open(output_file, "wb") as outfile:
            outfile.write(processed_data)

        print(f"[+] File '{filename}' {mode}ed successfully → '{output_file}'")

    except Exception as e:
        print(f"[-] Error while processing file: {e}")

def show_progress(message):
    print(f"{message}", end="", flush=True)
    for _ in range(3):
        print(".", end="", flush=True)
        time.sleep(0.4)
    print(" Done!")

def show_menu():
    print("\n" + "=" * 55)
    print("             SIMPLE XOR FILE ENCRYPTOR")
    print("=" * 55)
    print("1. Generate New Key")
    print("2. Encrypt a File")
    print("3. Decrypt a File")
    print("4. Exit")
    print("=" * 55)

def main():
    while True:
        show_menu()
        choice = input("Enter your choice (1-4): ").strip()

        if choice == "1":
            generate_key()

        elif choice == "2":
            key_value = load_key()
            if not key_value:
                continue
            filename = input("Enter the file name to encrypt: ").strip()
            show_progress("Encrypting")
            process_file(filename, key_value, "encrypt")

        elif choice == "3":
            key_value = load_key()
            if not key_value:
                continue
            filename = input("Enter the file name to decrypt: ").strip()
            show_progress("Decrypting")
            process_file(filename, key_value, "decrypt")

        elif choice == "4":
            print("\nExiting program", end="")
            for _ in range(3):
                print(".", end="", flush=True)
                time.sleep(0.4)
            print("\nGoodbye, have a great day!")
            sys.exit()

        else:
            print("[-] Invalid choice! Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
