# Sortarea a x elemente introduse de utilizator de la tastatura printr-o bucla while.
# Reprezinta aplicarea cunostintelor din sedinta 2 a cursului Python 007
# Oana Popa 11/10/15

n = int(raw_input("Scrie, te rog, cate elemente doresti sa introduci in lista: "))
l = []
while n > 0:
    elem = raw_input("Scrie, te rog, ce element doresti sa introduci in lista: ")
    l.append(elem)
    n -= 1
l.sort()
print "Lista cu care s-a lucrat si care a fost sortata este: ", l

raw_input("\n\nApasa <enter> pt a iesi.")
