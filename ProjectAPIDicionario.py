import requests
import json

y = 1

while y==1:
    x = input("\nDigite a palavra que desejar:")
    dicio_sig = requests.get(f"https://significado.herokuapp.com/v2/{x}")
    dicio_sig = dicio_sig.json()

    dicio_sin = requests.get(f"https://significado.herokuapp.com/v2/sinonimos/{x}")
    dicio_sin = dicio_sin.json()

    print("\nSignificados:\n")

    for i in range(len(dicio_sig)):
        print(f"{dicio_sig[i]}\n")

    print("Sinonimos:\n")

    print(f"{dicio_sin}\n")

    z = input("Digite 'S' caso queira procurar outra palavra, caso contrário digite qualquer valor.\n")
    if z == 'S' or z == 's':
        pass
    else:
        y = 0
        print("Obrigado!")
