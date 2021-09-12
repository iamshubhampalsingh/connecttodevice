import uiautomator2 as u2
from subprocess import check_output, CalledProcessError
def getDevice():
        try:
            adb_ouput =check_output(["adb", "devices"])
            try:
                encodeName=adb_ouput.split()[4]
                try:
                    deviceName=encodeName.decode("utf-8")
                    device=u2.connect(deviceName)
                    print(deviceName," Device Connected Successfully")
                    return device
                except RuntimeError as r:
                    print("Error While Connecting the device\n",r)
            except:
                print('Device Not Connected to the System')
        except:
                print('Device Not Connected to the System')