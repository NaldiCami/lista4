listaNomes =[]
for i in range(4):
    x = input("Digite um nome para adicionar na lista: ")
    x = x.upper()
    listaNomes.append(x)
n = input("Digite seu nome: ")
n = n.upper()
if n not in listaNomes:
    print("Seu nome não está na lista")
else:
    print("Seu nome está na lista")