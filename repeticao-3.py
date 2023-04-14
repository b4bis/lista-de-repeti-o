print ("nome:")
nome = input()
while len(nome) <3:
    print ("numero de caracteres invalido")
    nome = input()
print ("nome valido")

print ("idade:")
idade = int(input())
while idade <0 or idade >150:
    print ("idade invalida")
    idade = int(input())
print ("idade valida")

print ("salario")
salario = int(input())
while salario <= 0:
    print("salario invalido")
    salario = int(input())
print ("salrio valido")

generos = ["f", "m"]
print("f ou m")
sexo = input()
while not sexo in generos:
    print("f ou m")
    sexo = input()

EstadoCivil = ["S", "C", "V", "D"]
print ("Estado Civil")
EstadoCivil1 = input()
while not EstadoCivil1 in EstadoCivil:
    print("estado civil invalido")
    EstadoCivil1 = input()


