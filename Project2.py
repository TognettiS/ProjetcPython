y=0
notas=[]
i=0
media = 0

print("Digite suas 3 notas para calcular a média")
print("")

while True:

    if y>=0:
        digitar = input("Digite as notas:")
        print("")
        notas.append(float(digitar))
        media=media+notas[y]
        y = y + 1

        if y == 3:
            media=media/3
            print("A sua média é:",media)
            break
