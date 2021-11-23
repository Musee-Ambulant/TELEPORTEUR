import win32api
import win32file

drive_list = win32api.GetLogicalDriveStrings()
drive_list = drive_list.split("\x00")[0:-1]
drives = []
for drive in drive_list:
    if win32file.GetDriveType(drive) == win32file.DRIVE_REMOVABLE:  # check if the drive is of type removable
        print(drive ,"is a removable drive")
        drives.append(drive)

print(drives[0])


