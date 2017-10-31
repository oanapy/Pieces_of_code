# Crearea unei functii care sa inlocuiasca caracterele de tip spatiu cu underline si sa inlocuiasca sirul de caractere
#  <<e>> cu sirul de caractere <<i>> dintr-un sir de caractere primit ca parametru
# Reprezinta aplicarea cunostintelor din sedinta 3 a cursului Python 007
# Oana Popa 16/10/15


def replacer(string):
    # string = raw_input("Insert your string: ")
    li = []
    if type(string) == type("a"):
        for i in range(len(string)):
            li.append(string[i])
            if li[i] == "e":
                li[i] = "i"
            elif li[i] == " ":
                li[i] = "_"
    elif string == "":
        print "Dati va rog un sir de caractere"
    print "".join(li)

replacer ("Merele, perele si pestele nu au E-uri")

