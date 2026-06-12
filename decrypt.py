from locker import decrypt_file
import os

# Step 1: Load the secret key from .secret.key file
with open(".secret.key", "rb") as f:
    key = f.read()

# Step 2: Path of folder to decrypt
folder_path = "MY_Secret_Code"

# Step 3: Loop through files and decrypt them
for filename in os.listdir(folder_path):
    file_path = os.path.join(folder_path, filename)
    try:
        decrypt_file(file_path, key)  # Pass correct key here
        print(f"[OK] {filename} decrypted.")
    except Exception as e:
        print(f"[ERROR] Cannot decrypt {file_path}: {e}")

print("[DONE] Folder decrypted successfully.")
