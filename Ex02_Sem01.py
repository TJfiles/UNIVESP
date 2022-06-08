'''
Cap. 4 – Ex 3c
Realizar a leitura dos valores de quatro notas escolares bimestrais de um aluno representadas
pelas variáveis N1, N2, N3 e N4. Calcular a média aritmética (variável MD) desse aluno e apresentar a mensagem
“Aluno Aprovado com média” se a média obtida for maior ou igual a 5;
caso contrário, apresentar a mensagem “Aluno Reprovado com média”.
Informar também, após a apresentação das mensagens, o valor da média obtida pelo aluno
'''
N1 = float(input("Informe a primeira nota: "))
N2 = float(input("Informe a segunda nota: "))
N3 = float(input("Informe a terceira nota: "))
N4 = float(input("Informe a quarta nota: "))
print()
MD = (N1+N2+N3+N4)/4
if MD >= 5:
    print("Aluno Aprovado com média \n")
else:
    print("Aluno Reprovado com média \n")
print(f'A média do aluno foi: {MD}')
