# Exersarea lucrului cu modulele telnetlib si re
# Reprezinta aplicarea cunostintelor din sedinta 6 a cursului Python 007
# Oana Popa 07/11/15

import telnetlib, re
debugl = 0
HOST = "route-views.routeviews.org"
user = "rviews"
password = ""
print "Connecting..."
telnet_obj = telnetlib.Telnet(HOST)
telnet_obj.set_debuglevel(debugl)

# login - user
telnet_obj.read_until("login: ", 5)
telnet_obj.write(user + "\r\n")

print "Pass Validating..."

# login - pass
telnet_obj.read_until("password: ", 5)
telnet_obj.write(password + "\r\n")

print "Beginning input..."
telnet_obj.write("show version" + "\r\n")

cap = telnet_obj.read_until("--more--", 10)

to_show = re.search("Version " + "(\w+)" + "." + "(\w+)" + "." + "(\w+)", cap)
if to_show:
    print(to_show.group(0))

telnet_obj.close()

# raw_input("\n\nPress <enter> for exit.")
