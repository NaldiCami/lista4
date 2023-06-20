lista = []
listaImpar = []
for i in range(4):
    lista.append(input("Digite uma palavra: "))
    if len(lista[i])%2!=0:
        listaImpar.append(lista[i])

print("\nLista completa:",lista)
print("Palavras com número impar de letras:",listaImpar)
print("")