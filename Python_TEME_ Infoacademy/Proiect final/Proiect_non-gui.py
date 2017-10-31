# Proiect final - NON-GUI
# Aplicarea cunostintelor din cele 8 sedinte de Python
# Oana Popa 13/11/2015


#  creating a telnet session
def tn_login():
    import telnetlib
    # creating the telnet object
    host = "route-views.routeviews.org"
    telnet_obj = telnetlib.Telnet(host)
    # the default debug level
    debug_l = 0
    print "Connecting to telnet..."
    telnet_obj.set_debuglevel(debug_l)
    # credentials for the telnet login
    user = "rviews"
    password = ""
    # login - user
    telnet_obj.read_until("login: ", 5)
    telnet_obj.write(user + "\r\n")
    print "Pass Validating..."
    # login - pass
    telnet_obj.read_until("password: ", 5)
    telnet_obj.write(password + "\r\n")
    # write in the telnet
    print "Beginning input..."
    telnet_obj.write("show ip route 192.0.2.1" + "\r\n")
    # capture the telnet message
    cap = telnet_obj.read_until("--more--", 10)
    # close the telnet object
    telnet_obj.close()
    return cap
# a variable to store the capture of the tn_login() function
tn_login_output = tn_login()


# works with the capture from the tn_login
def tn_cap():
    import re
    # applying the re search for the telnet's capture
    print "Search for the requested string..."
    to_show = re.search('Known via' + "(\W+)" + "(\D+)" + "(\W+)" + "(\d+)" + "(\W)", tn_login_output)
    # if the search string exists, return it via group, if not, return False
    if to_show:
        return to_show.group(0)
    else:
        return False
# a variable to store the capture of the tn_cap() function
tn_cap_output = tn_cap()


# extracts the time from the pool.ntp.org server
def ntp_time():
    import ntplib
    import time
    # creating the ntp object
    c = ntplib.NTPClient()
    # if the searched string from the capture exists
    if tn_cap_output:
        try:
            # asks the server for the time and transforms it into a human readable form
            response = c.request('2.ro.pool.ntp.org', 2)
            print "Ask the time from the server..."
            return time.ctime(response.tx_time)
        except(), e:
            return "Eroare: timpul nu a putut fi extras cel mai probabil din cauza unei probleme de retea!", e
# a variable to store the capture of the tn_cap() function
ntp_time_output = ntp_time()


# creates a smtp mail session
def smtp_mail(str1, str2):
    import smtplib
    # creating the smtp object
    smtp_obj = smtplib.SMTP('smtp.gmail.com:587')
    # str1 = ntp_time_output, str2 = tn_cap_output
    # if the searched string exists, send it in my email
    if str2:
        mesaj = """From: mail.through.python@gmail.com
        To: Me
        Subject: SMTP e-mail test - Python Force!
        Content-type: text/html

        Timpul serverului indicat este %s, iar raspunsul primit prin telnetlib este %s
        """ % (str1, str2)
    # if the searched string does NOT exist, send some attention message
    else:
        mesaj = """From: mail.through.python@gmail.com
        To: Me
        Subject: SMTP e-mail test - Python Force!
        Content-type: text/html

        Informatia nu a fost gasita!
        """
    # details about the sender
    sender = "mail.through.python@gmail.com"
    # credentials for the gmail login
    username_sender = 'mail.through.python'
    pass_sender = 'infoacad'
    # the receiver
    receiver = ['popa.gina.oana@gmail.com']
    try:
        smtp_obj.starttls()
        # logs into the mail account
        smtp_obj.login(username_sender, pass_sender)
        # sends the message
        smtp_obj.sendmail(sender, receiver, mesaj)
        print "Mesajul electronic a fost trimis cu succes"
    except(), e:
        print "Mesajul electronic nu a fost trimis cu succes"
        print e
    else:
        # closes the smtp session if the try actions are a success
        smtp_obj.quit()


# checks if everything went well
smtp_mail(ntp_time_output, tn_cap_output)

raw_input("\n\nPress <enter> for exit.")
