# kimsufi-hunter
**Kimsufi Hunter** - a script catching chance to buy cheap dedicated server. 

Meant to be very simple - just run and wait for email ;)

### Configuration
    TARGET_KIMSUFI_ID  - set to ID from https://www.kimsufi.com/en/ source code (eg. 150sk40 is KS-1)
    TARGET_DESCR       - human readable description (eg. KS-1)
    EMAIL_FROM_ADDRS   - email "from"
    EMAIL_TO_ADRS      - target email address
    EMAIL_SMTP_LOGIN   - SMTP login (probably equal to EMAIL_FROM_ADDRS)
    EMAIL_SMTP_PASSWD  - SMTP password
    EMAIL_SMTP_SERVER  - SMTP server with port number (smtp.gmail.com:587 for gmail)

### Environment
**Python 3.4** on some 24/7 running machine (eg. VPS, home nettop) + SMTP account.
I recommend using dedicated gmail account for SMTP (it's portable; using own primary account would affect security).

### What is all about?
+ Kimsufi homepage - https://www.kimsufi.com/en/
+ Something more (in Polish) on my blog - http://blog.dsinf.net/2015/01/kimsufi-hunter/
