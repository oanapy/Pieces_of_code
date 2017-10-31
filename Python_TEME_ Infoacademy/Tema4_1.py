# Crearea a 3 clase ce vor reprezenta un catalog auto.
# Reprezinta aplicarea cunostintelor din sedinta 4 a cursului Python 007
# Oana Popa 25/10/15


class First_C(object):
    def __init__(self, marca, tip):
        self.m = marca
        self.t = tip

    def Culoare(self, culoare):
        self.c = culoare

    def AfisareCaracteristici(self):
        print "Culoarea masinii pentru masina marca", self.m, "si tipul", self.t, "este", self.c


class Second_C(First_C):
    def Optiunea1(self, scaune_incalzite):
        self.s = scaune_incalzite


class Third_C(First_C):
    def Optiunea2(self, blocuri_optice_LED):
        self.b = blocuri_optice_LED

raw_input("\n\nPress <enter> for exit.")
