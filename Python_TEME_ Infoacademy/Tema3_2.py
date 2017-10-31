# Lucrul cu dictionare.
# Reprezinta aplicarea cunostintelor din sedinta 3 a cursului Python 007
# Oana Popa 16/10/15


d = {1: "Unu",
     2: "Doi Doi",
     3: "Trei Trei Trei"
     }
# Printati fiecare pereche de tip cheie valoare din dictionar printr-un for.
for i in d:
    print i, d[i]
# Solicitati userului sa introduca text de la tastatura. Acest text devine valoarea unei noi intrari in dictionar ce
# va avea cheia 4.
inp = raw_input("Enter your desired text: ")
d[4] = inp
# Printati fiecare pereche de tip cheie valoare din dictionar printr-un for.
for i in d:
    print i, d[i]
# Stergeti intrarea ce are cheia cu numarul 2.Printati fiecare pereche de tip cheie valoare din dictionar printr-un for.
del(d[2])
for i in d:
    print i, d[i]


raw_input("\n\nPress <enter> for exit.")
