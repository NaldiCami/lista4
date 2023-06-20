lista = []

for i in range(5):
    lista.append(int(input("Digite um número: ")))

media = sum(lista)/len(lista)
print(media)