print ("digite 5 numeros")
numeros = []
for i in range(5):
    numero = float(input(f"digite o numero {i+1}:"))
    numeros.append(numero)

soma = sum(numeros)

media = soma / len(numeros)

print("a soma dos numeros é:", soma )
print("a media é", media )