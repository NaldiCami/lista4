lista = []
listaDiv = []
for i in range(4):
    lista.append(int(input("Digite um número para entrar na lista: ")))
divisor = int(input("Digite um número que você gostaria que fosse o divisor: "))

for i2 in range(4):
    if lista[i2]%divisor==0:
        listaDiv.append(lista[i2])

print("\nEssa é a lista completa: ",lista)
print("Esses são os números dela que são divisiveis por",divisor,":",listaDiv)
print("")