notas= [3, 6, 9, 10]
media= 0
for i in range(0, len(notas)):
    print("nota", i+1, ":" , notas[i])
    media = media + notas [i]
media = media / len(notas)
print("media:", media)
