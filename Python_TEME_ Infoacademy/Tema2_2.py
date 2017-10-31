# Crearea unui program cu o lista de cumparaturi utilizand dictionare.
# Reprezinta aplicarea cunostintelor din sedinta 2 a cursului Python 007
# Oana Popa 11/10/15

l = {}

print"\t\t Bine ati venit la programul lista de cumparaturi utilizand dictionare"

while True:
    print """
    Alegeti una din optiunile de mai jos, inserand cifra corespunzatoare:
0 - Pentru afisarea dictionarului actual
1 - Pentru introducerea unui element nou in dictionar
2 - Pentru stergerea unui element existent
3 - Pentru stergerea intregului dictionar
q - Pentru iesirea din program
"""
    alegere = raw_input("\nIntrodu o cifra:\t")

    if alegere == "0":
        if l:
            print "\nDictionarul de cumparaturi este :\n"
            for key in sorted(l):
                print "%s => %s" % (key, l[key])
        else:
            print "Dictionarul este gol"
    elif alegere == "1":
        n = int(raw_input("Cate elemente doresti sa introduci? Scrie raspunsul aici: "))
        for i in range(n):
            elem = raw_input("Scrie, te rog, ce element doresti sa introduci in dictionar: ")
            l[str(i)] = elem
    elif alegere == '2':
        if l:
            rem = raw_input("Scrie, te rog, ce element doresti sa stergi in dictionar,"
                            " introducand cifra din fata acestuia: ")
            if rem in l:
                del l[rem]
                print "Elementul ", rem, "a fost sters"
            else:
                print rem, "nu a fost gasit in dictionar"
        else:
            print "Dictionarul este gol"
    elif alegere == '3':
        l = {}
        print "Dictionarul a fost sters"
    elif alegere.upper() == 'Q':
        break

print "Va multumim ca ati ales acest program"

raw_input("\n\nApasa <enter> pt a iesi.")
