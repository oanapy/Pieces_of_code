# Lucrul cu try-except-else.
# Reprezinta aplicarea cunostintelor din sedinta 4 a cursului Python 007
# Oana Popa 25/10/15


class Adunare():
    def __init__(self, a, b):
        self.a = a
        self.b = b
        try:
            c = self.a + self.b
        except Exception, e:
            print "Nu se poate adunare"
            # print e
        else:
            print "Suma este:" + str(c)

    def __str__(self):

        try:
            c = self.a * self.b
        except Exception, f:
            return "Nu se poate inmultire"
            # return f
        else:
            return "Produsul este:" + str(c)

o1 = Adunare(1, 12)
# o1
print o1
o2 = Adunare("1", 12)
# o2
print o2
o3 = Adunare("1", "12")
# o3
print o3



raw_input("\n\nPress <enter> for exit.")