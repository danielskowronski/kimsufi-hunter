# python kimsufi hunter v0.1

# CONFIG
TARGET_KIMSUFI_ID = "" # something like 150sk40
TARGET_DESCR      = ""
EMAIL_FROM_ADDRS  = ""
EMAIL_TO_ADRS     = ""
EMAIL_SMTP_LOGIN  = EMAIL_FROM_ADDRS
EMAIL_SMTP_PASSWD = ""
EMAIL_SMTP_SERVER = "" # somthing like smtp.gmail.com:587

# CODE
import urllib.request
import smtplib
import time

def isAvailable():
    rawPageContent = urllib.request.urlopen("https://www.kimsufi.com/en/").read()
    rawPageContent = str(rawPageContent)
    poz = rawPageContent.find(TARGET_KIMSUFI_ID)
    row = rawPageContent[poz:]
    poz = row.find("</tr>")
    row = row[:poz]
    searchText = "Currently being replenished"
    poz = row.find(searchText)
    return poz != -1

def sendEmailWithMessageAvailable():
    msg = "From: KIMSUFI HUNTER <"+EMAIL_FROM_ADDRS+">\r\n"+\
        "To: "+EMAIL_TO_ADRS+"\r\n"+\
        "Subject: [KIMSUFI] "+TARGET_DESCR+" is now AVAILABLE!\r\n"+\
        "\r\n"+\
        "kimsufi-hunter.py has detected that "+TARGET_DESCR+" is now ["+time.ctime()+"] available!\r\n"+\
        "https://www.kimsufi.com/en/\r\n"
    server = smtplib.SMTP(EMAIL_SMTP_SERVER)
    server.starttls()
    server.login(EMAIL_SMTP_LOGIN,EMAIL_SMTP_PASSWD)
    server.sendmail(EMAIL_FROM_ADDRS, EMAIL_TO_ADRS, msg)
    server.quit()

while True:
    if isAvailable():
        print(time.ctime() + " -- KIMSUFI "+TARGET_DESCR+" not available")
        nextSleep = 5 #5secs
    else:
        print(time.ctime() + " -- KIMSUFI "+TARGET_DESCR+" AVAILABLE!!! -- sleeping for 5 minutes")
        sendEmailWithMessageAvailable()
        nextSleep = 5*60 #5mins
    time.sleep(nextSleep)
