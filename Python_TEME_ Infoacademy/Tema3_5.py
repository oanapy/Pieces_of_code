# Crearea unei clase ce va reprezenta un catalog
# Reprezinta aplicarea cunostintelor din sedinta 3 a cursului Python 007
# Oana Popa 16/10/15


class Catalog:
    def __init__(self, n, pren):
        self.nume = n
        self.prenume = pren

    def abs_plus(self, abst):
        self.absente = int(abst) + 1

    def abs_minus(self, abste):
        if type(abste) == type(2):
            self.absente -= abste
            if self.absente < 0:
                self.absente = 0

    def __str__(self):
        return "Numarul de absente pentru elevul {} {} este {}.".format(str(self.nume), str(self.prenume),
                                                                        str(self.absente))


elev1 = Catalog("Ion", "Roata")
elev1.abs_plus(3)
elev1.abs_minus(6)

elev2 = Catalog("George", "Cerc")
elev2.abs_plus(3)
elev2.abs_minus(2)

print elev1
print elev2

raw_input("\n\nPress <enter> for exit.")
