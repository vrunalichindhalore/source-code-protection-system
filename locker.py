from cryptography.fernet import Fernet
import os

def generate_key():
    key = Fernet.generate_key()
    with open(".secret.key", "wb") as key_file:
        key_file.write(key)
    return key

def load_key():
    with open(".secret.key", "rb") as key_file:
        return key_file.read()

def encrypt_file(file_path, key):
    f = Fernet(key)
    with open(file_path, "rb") as file:
        data = file.read()
    encrypted = f.encrypt(data)
    with open(file_path + ".encrypted", "wb") as file:
        file.write(encrypted)
    os.remove(file_path)

def decrypt_file(file_path, key):
    f = Fernet(key)
    with open(file_path, "rb") as file:
        data = file.read()
    decrypted = f.decrypt(data)
    original_path = file_path.replace(".encrypted", "")
    with open(original_path, "wb") as file:
        file.write(decrypted)
    os.remove(file_path)

def encrypt_folder(folder_path, key):
    for root, _, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            encrypt_file(file_path, key)

def decrypt_folder(folder_path, key):
    for root, _, files in os.walk(folder_path):
        for file in files:
            if file.endswith(".encrypted"):
                file_path = os.path.join(root, file)
                decrypt_file(file_path, key)
