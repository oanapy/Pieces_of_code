# Crearea unui program ce imparte sirul de caractere <<Avem ce face in Python>> intr-o lista.
# Reprezinta aplicarea cunostintelor din sedinta 3 a cursului Python 007
# Oana Popa 16/10/15

sir = "Avem ce face in Python"
li = []
for i in range(len(sir)):
    li.append(sir[i])
    if li[i] == "e":
        li[i] = "i"
    elif li[i] == " ":
        li[i] = "_"

print "The joined list is ", "".join(li)


raw_input("\n\nPress <enter> for exit.")
