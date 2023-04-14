print ("digite 5 numeros")
numeros = []
for i in range(5):
    numero = float(input(f"digite o numero {i+1}:"))
    numeros.append(numero)

maiornumero = max(numeros)

print("o maior numero é:", maiornumero )