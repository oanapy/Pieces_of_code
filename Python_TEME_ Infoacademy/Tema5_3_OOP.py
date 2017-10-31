# Crearea unui program randomic - OOP
# Reprezinta aplicarea cunostintelor din sedinta 5 a cursului Python 007
# Oana Popa 31/10/15


class whatDay():

    def __init__(self):
        self.lst = []
        self.an = 0
        self.lu = 0
        self.zi = 0

    def __aleatoriu(self):
        import random
        self.an = random.randrange(2000, 2020)
        self.lu = random.randrange(1, 12)
        self.zi = random.randrange(1, 28)
        self.lst.append(self.an)
        self.lst.append(self.lu)
        self.lst.append(self.zi)

    def day(self):
        import calendar
        zile = ["Luni", "Marti", "Miercuri", "Joi", "Vineri", "Sambata", "Duminica"]
        whatDay.__aleatoriu(self)
        zi = calendar.weekday(self.lst[0], self.lst[1], self.lst[2])
        if zi+1 == 1:
            print "Ziua aleatoriu aleasa este prima zi (",zile[0] ,") a saptamanii."
        else:
            print "Ziua aleatoriu aleasa este a", zi+1, "zi (",zile[zi],") a saptamanii."
