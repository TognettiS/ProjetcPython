Dicionario = {
 "Ambulância" : "Qualquer estabelecimento de saúde ambulante.",
 "Blusa": "Veste de pano, geralmente larga, usada sobre outra roupa para protegê-la.",
 "Conciso": "Reduzido ao essencial, em poucas palavras (diz-se de escritos, ideias, discurso etc.), preciso, sucinto, resumido."
}

#print (Dicionario)

# for palavras in Dicionario:
#     print (palavras)

# Dicionario ["Dinâmico"] = "Que se modifica continuamente, que evolui; que pressupõe movimento, mudança."
#
# for palavras in Dicionario:
#     significado = Dicionario[palavras]
#     print (significado)

# Dicionario.pop("Blusa")
# print(Dicionario.values())

# if "Panela" in Dicionario:
#     print("Essa palavra foi encontrada")
# else:
#     print("Palavra não localizada")

if "Veste de pano, geralmente larga, usada sobre outra roupa para protegê-la." in Dicionario.values():
    print("Definição encontrada")
else:
    print("Definição não localizada")
