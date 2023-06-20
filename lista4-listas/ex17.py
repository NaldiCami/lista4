lista = []
listaE = []
for i in range(4):
    n = input("Digite um nome: ")
    n = n.upper()
    lista.append(n)

for i2 in range(4):
    palavra = lista[i2]
    cLetra = len(palavra)
    for i3 in range(cLetra):
        if palavra[i3] == "E":
            listaE.append(palavra)
