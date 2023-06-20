lista = []
lista3 = []
for i in range(4):
    lista.append(int(input("Digite um número: ")))
    if lista[i]%3==0:
        lista3.append(lista[i])

print(lista)
print(lista3)
print("")