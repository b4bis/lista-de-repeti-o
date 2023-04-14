numero1 = int(input("Digite o primeiro número inteiro: "))
numero2 = int(input("Digite o segundo número inteiro: "))

menor = min(numero1, numero2)
maior = max(numero1, numero2)

print("Números inteiros no intervalo entre", menor, "e", maior, ":")
for i in range(menor, maior + 1):
    print(i)