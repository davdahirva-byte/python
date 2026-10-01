f1 = open("abc", "r")

data = f1.read()

space = True

for x in data:
    if space == True:
        print(x.upper(), end="")
        space = False
    else:
        print(x, end="")

    if x == " ":
        space = True

f1.close()