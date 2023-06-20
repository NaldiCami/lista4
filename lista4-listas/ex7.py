lista=[]

for i in range(4):
    lista.append(input("Digite um nome: "))
lmaior = max(lista,key=len)
lmenor = min(lista,key=len)

print("Esse é o maior nome:",lmaior)
print("Esse é o menor nome:",lmenor)
