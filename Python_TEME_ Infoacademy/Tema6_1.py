# Exersarea lucrului cu modulul re
# Reprezinta aplicarea cunostintelor din sedinta 6 a cursului Python 007
# Oana Popa 07/11/15

import os, re
print "Aplicam comanda date /t in consola"

stdin, stdout = os.popen2('date /t')
stdin.close()

print "Citim output"
captura = stdout.read()

print "Afisam output"
print captura

print "Cautam cu ajutorul modulului re anul curent"
cauta = re.search("(2\d+)", captura)
if cauta:
    print cauta.group(0)
