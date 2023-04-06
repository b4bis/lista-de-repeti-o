numeros= [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
pares = []
impares = []
for i in numeros:
    if numeros[i-1]%2:
        impares.append(numeros[i-1])
    else:
        pares.append(numeros[i-1])
print("numeros:", numeros)
print("pares:",pares)
print("impares:", impares)
