import subprocess

def get_usb_serial():
    try:
        output = subprocess.check_output('wmic diskdrive where "InterfaceType=\'USB\'" get SerialNumber', shell=True)
        lines = output.decode().splitlines()
        for line in lines:
            serial = line.strip()
            if serial and "SerialNumber" not in serial:
                print("USB Serial Number:", serial)
    except Exception as e:
        print("Error:", e)

get_usb_serial()
