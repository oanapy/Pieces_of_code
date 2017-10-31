# Lucrul cu functii
# Reprezinta aplicarea cunostintelor din sedinta 3 a cursului Python 007
# Oana Popa 16/10/15


def calc(a, b,c):
    res = (int(a) * (int(a) + 3) / int(b)) * int(c)
    print res

calc(1, 2, 3)
# For not dealing with errors, I chose to transform the str in int
calc("1", "2", "3")


raw_input("\n\nPress <enter> for exit.")
