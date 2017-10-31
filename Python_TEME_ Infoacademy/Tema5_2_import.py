# Crearea unui fisier ce importa modulul Tema5_2
# Reprezinta aplicarea cunostintelor din sedinta 5 a cursului Python 007
# Oana Popa 31/10/15

# import al modulelor sys si os
import sys, os
if sys.platform == "win32":
    # import al noului modul creat
    import Tema5_2
    # identificarea directorului de lucru
    cale_now = os.getcwd()
    print "Calea curenta este: ", cale_now
    print "Calea va fi schimbata la 'C:\Program Files'. Esti de acord?"
    # confirmarea schimbarii caii
    ans = raw_input("Introdu da/nu:")
    if ans == "da" or ans == "d":
        # modificarea directorului de lucru
        os.chdir("C:\Program Files")
    else:
        print "Calea nu va fi schimbata."
    print "Calea a fost schimbata la 'C:\Program Files' "
    print "Rezultatul functiei Adunare este: ", Tema5_2.Adunare("2", "3")
else:
    print "Acest modul poate fi rulat doar sub Windows OS"
    # iesirea din program
    sys.exit()

raw_input("\n\nPress <enter> for exit.")
