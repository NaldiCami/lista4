palavras = []
palavrasA = []
i = 0
while i <4:
    n = input("Digite uma palavra: ")
    n = n.upper()
    palavras.append(n)
    i+=1

print(palavras)

j = 0
while j <4:
    x = palavras[j]
    x = x[0]
    if x == "A":
        palavrasA.append(palavras[j])
    j+=1
print(palavrasA)
