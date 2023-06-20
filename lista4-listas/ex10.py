lista =[]
for i in range(4):
    lista.append(int(input("Digite um número: ")))

lista = list(set(lista))
lista.sort()
print(lista)
