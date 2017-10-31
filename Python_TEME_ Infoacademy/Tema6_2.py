# Exersarea lucrului cu modulele time, ntplib si smtplib
# Reprezinta aplicarea cunostintelor din sedinta 6 a cursului Python 007
# Oana Popa 07/11/15

import ntplib, time, smtplib
c = ntplib.NTPClient()
response = c.request('2.ro.pool.ntp.org', 2)
# print time.ctime(response.tx_time)

sender = "mail.through.python@gmail.com"
receiver = ['popa.gina.oana@gmail.com']

mesaj = """From: mail.through.python@gmail.com
To: Me
Subject: SMTP e-mail test - Python Force!
Content-type: text/html

Timpul serverului indicat este %s
""" % (time.ctime(response.tx_time))

# Gmail Login
username_sender = 'mail.through.python'
pass_sender = 'infoacad'
# debug_pass = '****'

try:
    smtpObj = smtplib.SMTP('smtp.gmail.com:587')
    smtpObj.starttls()
    smtpObj.login(username_sender, pass_sender)
    smtpObj.sendmail(sender, receiver, mesaj)
    print "Mesajul electronic a fost trimis cu succes"
except(), e:
    print "Mesajul electronic nu a fost trimis cu succes"
    print e
else:
    smtpObj.quit()


raw_input("\n\nPress <enter> for exit.")
