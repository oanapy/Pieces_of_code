# Crearea unui program cu o lista de CD/DVD-uri utilizand dictionare si liste
# Reprezinta aplicarea cunostintelor din sedinta 2 a cursului Python 007
# Oana Popa 11/10/15


l = {}

print"\t\t Bine ati venit la programul lista de CD/DVD-uri utilizand dictionare si liste"

while True:
    print """
    Alegeti una din optiunile de mai jos, inserand cifra corespunzatoare:
0 - Pentru afisarea dictionarului actual
1 - Pentru introducerea unui element nou in dictionar
2 - Pentru stergerea unui element existent
3 - Pentru stergerea intregului dictionar
4 - Pentru a cauta un element in dictionar
q - Pentru iesirea din program
"""
    alegere = raw_input("\nIntrodu o cifra:\t")

    if alegere == "0":
        if l:
            print "\nDictionarul de CD/DVD este :\n"
            for key in sorted(l):
                print "%s => %s" % (key, l[key])
        else:
            print "Dictionarul este gol"
    elif alegere == "1":
        elem_title = raw_input("Scrie, te rog, ce titlu doresti sa introduci in dictionar: ")
        elem_content = raw_input("Scrie, te rog, ce continut doresti sa introduci in dictionar: ")
        i = 0
        while True:
            if not l.has_key(i):
                cheie = i
                break
            i += 1

        l[cheie] = [elem_title, elem_content]
        print "\nIntrarea adaugata este:"
        print cheie, "  => ", l[cheie][0], l[cheie][1]
    elif alegere == '2':
        if l:
            print "Momentan, continutul dictionarului este ",
            for key in sorted(l):
                print "%s => %s" % (key, l[key])
            rem = raw_input("Scrie, te rog, ce element doresti sa stergi in dictionar, "
                            "introducand cifra din fata acestuia: ")
            if int(rem) in l.keys():
                del l[int(rem)]
                print "Elementul ", rem, "a fost sters"
            else:
                print rem, "nu a fost gasit in dictionar"
        else:
            print "Dictionarul este gol"
    elif alegere == '3':
        l = {}
        print("Dictionarul a fost sters")
    elif alegere == '4':
        alg = raw_input("Introdu titlul sau continutul itemului cautat: ")
        for key, value in l.items():
            for v in value:
                if alg in v:
                    print "Elementul cautat ", alg, "a fost gasit "
    elif alegere.upper() == 'Q':
        break

print "Va multumim ca ati ales acest program"

raw_input("\n\nApasa <enter> pt a iesi.")
