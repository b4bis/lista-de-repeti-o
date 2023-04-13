aluno1 = [10,7,7,6]
aluno2 = [3,6,4,9]
aluno3 = [7,7,8,10]
aluno4 = [5,7,5,2]
aluno5 = [9,6,9,7]
aluno6 = [10,9,8,7]
aluno7 = [10,9,9,10]
aluno8 = [5,8,2,7]
aluno9 = [9,9,8,9]
aluno10 = [8,7,6,9]
alunos = [aluno1, aluno2, aluno3, aluno4, aluno5,aluno6, aluno7, aluno8, aluno9, aluno10]
contagem = 0
final = ""
media = 0
for i in alunos:
    for nota in alunos [contagem]:
        media = media + nota
    media = media / len(alunos[contagem]) 
    if media >= 7:
        final = f"{final} aluno {contagem+1} (aprovado) - {media} |"
    contagem += 1
    media = 0
    print("medias:", final)