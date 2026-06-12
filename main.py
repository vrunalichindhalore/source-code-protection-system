import subprocess
import time
import os
from locker import encrypt_folder, generate_key

FOLDER_PATH = "MY_Secret_Code"
AUTHORIZED_SERIAL = "4C530000200320202493"  # <-- yaha apna USB ka serial number daalo

def get_usb_serial():
    try:

        output = subprocess.check_output('wmic diskdrive where "InterfaceType=\'USB\'" get SerialNumber', shell=True)
        lines = output.decode().splitlines()

        for line in lines:
            serial = line.strip()
            if serial and "SerialNumber" not in serial:
                print("USB Serial Number:", serial)
                return serial
        return None
    except Exception as e:
        print("[ERROR] Serial fetch failed:", e)
        return None

def monitor_usb():
    print("[RUNNING] Monitoring USB devices... Press Ctrl+C to stop.")
    key = generate_key()

    while True:
        usb_serial = get_usb_serial()
        if usb_serial:
            if usb_serial == AUTHORIZED_SERIAL:
                print("[INFO] Authorized USB connected. No action taken.")
            else:
                print("[ALERT] Unauthorized USB detected! Encrypting folder...")
                encrypt_folder(FOLDER_PATH, key)
                print("[DONE] Folder encrypted.")
                break
        time.sleep(5)

if __name__ == "__main__":
    monitor_usb()
