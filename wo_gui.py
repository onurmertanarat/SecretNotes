from cryptography.fernet import Fernet

user_title = input("Enter your title: ")
user_secret_text = input("Enter your secret text: ")
user_master_key = input("Enter your master key: ")

key = Fernet.generate_key()
fernet = Fernet(key)

encrypt_text = fernet.encrypt(user_secret_text.encode())

print(f"Encrypted message: {encrypt_text}")

decrypt_text = fernet.decrypt(encrypt_text).decode()

while True:
    input_master_key = input("Enter your master key: ")
    if input_master_key == user_master_key:
        print(user_title)
        print(decrypt_text)
        break
    else:
        print("Invalid master key!")
