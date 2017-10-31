# Crearea unui program randomic
# Reprezinta aplicarea cunostintelor din sedinta 5 a cursului Python 007
# Oana Popa 31/10/15

def Aleatoriu():
    import random
    lst = []
    an = random.randrange(2000, 2020)
    lst.append(an)
    lu = random.randrange(1, 12)
    lst.append(lu)
    zi = random.randrange(1, 28)
    lst.append(zi)
    return lst

def Ce_zi():
    import calendar
    zile = ["Luni", "Marti", "Miercuri", "Joi", "Vineri", "Sambata", "Duminica"]
    res = []
    for i in range(3):
        a = Aleatoriu()
        res.append(a)
        day = calendar.weekday(res[i][0], res[i][1], res[i][2])
        if day+1 == 1:
            print "Ziua aleatoriu aleasa este prima zi (",zile[0] ,") a saptamanii."
        else:
            print "Ziua aleatoriu aleasa este a", day+1, "zi (",zile[day],") a saptamanii."

Ce_zi()