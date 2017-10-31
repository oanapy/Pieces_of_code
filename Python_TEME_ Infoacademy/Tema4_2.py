# Crearea unui fisier de tip ini numit Tema_Clasa cu anumite linii de continut.
# Reprezinta aplicarea cunostintelor din sedinta 4 a cursului Python 007
# Oana Popa 25/10/15

file1 = open("f.ini", "a+")
file1.write("Nume Prenume\n")
file1.write("ini, text sau txt\n")
file1.write("Citire\n")
file1.close()

file1 = open("f.ini", "a+")
print file1.readlines()
file1.close()

file1 = open("f.ini", "a+")
file1.write("EU SUNT 4\n")
file1.close()

file1 = open("f.ini", "a+")
print file1.read()
file1.close()

raw_input("\n\nPress <enter> for exit.")

