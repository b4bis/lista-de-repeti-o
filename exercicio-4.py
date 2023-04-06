vogais = ['a','e','i','o','u']
letras = ['m','n','p','q','r','s','t','u','v','w']
consoantes1 = []
consoantes = 0
contador = 0
for i in letras:
    if not letras [contador] in vogais:
        consoantes+= 1 
        consoantes1.append(letras[contador])
        print('consoantes:',consoantes)
        print('quais consoantes:', consoantes)
        