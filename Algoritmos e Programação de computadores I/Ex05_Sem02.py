'''Traduza os comandos a seguir para expressões Booleanas em Python e avalie-as:
(a) A soma de 2 e 2 é menor que 4.
(b) O valor de 7 // 3 é igual a 1 + 1.
(c) A soma de 3 ao quadrado e 4 ao quadrado é igual a 25.
(d) A soma de 2, 4 e 6 é maior que 12.
(e) 1387 é divisível por 19.
(f) 31 é par. (Dica: o que o resto lhe diz quando você divide por 2?)
(g) O preço mais baixo dentre R$ 34,99, R$ 29,95 e R$ 31,50 é menor que R$ 30,00.*
'''

#(a) A soma de 2 e 2 é menor que 4.
print(2+2 <4)

#(b) O valor de 7 // 3 é igual a 1 + 1.
print(7//3 == 1+1)

#(c) A soma de 3 ao quadrado e 4 ao quadrado é igual a 25.
print(((3**2)+(4**2))==25)

#(d) A soma de 2, 4 e 6 é maior que 12.
print((2+4+6)>12)

#(e) 1387 é divisível por 19.
print(1387%19==0)

#(f) 31 é par. (Dica: o que o resto lhe diz quando você divide por 2?)
print(31%2==0)

#(g) O preço mais baixo dentre R$ 34,99, R$ 29,95 e R$ 31,50 é menor que R$ 30,00.*
print(min(34.99,29.95,31.50)<30)