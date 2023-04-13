numeros= [1, 2, 3, 4, 5]
soma = 0
resultado = numeros[0]
print ("numeros inteitos", numeros)
for i in numeros:
    soma = soma + numeros[i-1]
    resultado = resultado * numeros[i-1] 
print (soma)
print ("Resultado da multiplicação",resultado)
