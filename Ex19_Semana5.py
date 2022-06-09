'''
Implemente a função med(), que aceita como entrada uma lista que contém listas de números. Cada lista de números representa as notas que determinado aluno recebeu para um curso. Por exemplo, aqui está uma lista de entrada para uma classe de quatro alunos:
[[95, 92, 86, 87], [66, 54], [89, 72, 100], [33, 0, 0]]
A função avg deverá exibir, uma por linha, a nota média de cada aluno. Você pode considerar que cada lista de notas não
é vazia, mas não deve considerar que todos alunos tem o mesmo número de notas
>>> med([[95, 92, 86, 87], [66, 54], [89, 72, 100], [33, 0, 0]])
90.0
60.0
87.0
11.0
'''

notas = [[95, 92, 86, 87], [66, 54], [89, 72, 100], [33, 0, 0]]

def med(lista):
    for aluno in lista:
        sum = 0
        for nota in aluno:
            sum += nota
            media = sum/len(aluno)
        print(media)

med(notas)