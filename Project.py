import random

num1 = random.randint(1,100)
print("Sorteador de números!")

x = int (input("Digite um número de 1 até 100:"))

y = 0


while (y==0):
    if x == num1:
        print("Acertou!")
        y=1
    elif x >= num1:
        print("Valor muito alto")
        x = int (input("Digite outro número:"))
    elif x <= num1:
        print("Valor muito baixo")
        x = int (input("Digite outro número:"))
