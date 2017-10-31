# Crearea unui modul
# Reprezinta aplicarea cunostintelor din sedinta 5 a cursului Python 007
# Oana Popa 31/10/15


def Adunare(p1, p2):
    try:
        s = p1 + p2
        return s
    except:
        return "Parametrii introdusi nu pot fi adunati!"

if __name__ == "__main__":
    print "Modulul trebuie importat! El nu poate fi rulat direct"
