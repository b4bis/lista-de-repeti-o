idades = []
altura = []
resultado = ""
for i in range(0,5):
    print("Insira a idade:")
    altura = input()
    print("Insira a altura:")
    altura = [altura, input()]
    idades.append(altura)
    altura = []
contador = len(idades)
for i in range(0,contador):
    resultado = f"{resultado} {idades[contador-1]}"
    contador -= 1
print(resultado)