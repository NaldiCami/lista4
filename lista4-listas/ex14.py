lista=[]
for i in range(4):
    lista.append(int(input("Digite um nome: ")))
lista.sort(reverse = True)
print(lista[-2])