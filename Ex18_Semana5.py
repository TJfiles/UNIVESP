'''
Escreva um programa que solicita um inteiro positivo de quatro dígitos do usuário e exibe seus dígitos. Você não poderá
usar as operações do tipo de dados string para realizar essa tarefa. Seu programa deverá simplesmente ler a entrada como
um inteiro e processá-la como um inteiro, usando as operações aritméticas padrão (+, *, -, /, % etc.).
>>>
Digite n: 1234
1
2
3
4
'''

numero = int(input('Digite n: '))

p = 1000
for i in range(4):
    primeiro = int(numero//p)
    numero = int(numero%p)
    p = p/10
    print(primeiro)

