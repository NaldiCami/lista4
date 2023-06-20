lista =[]
listaImpar = []
for i in range(4):
    lista.append(int(input("Digite um número: ")))
    if lista[i]%2!=0:
        listaImpar.append(lista[i])
print(sum(listaImpar))