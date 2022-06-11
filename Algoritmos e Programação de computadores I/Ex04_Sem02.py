'''
Exercício 2.1
Escreva expressões algébricas Python correspondentes aos seguintes comandos:
(a) A soma dos 5 primeiros inteiros positivos.
(b) A idade média de Sara (idade 23), Mark (idade 19) e Fátima (idade 31).
(c) O número de vezes que 73 cabe em 403.
(d) O resto de quando 403 é dividido por 73.
(e) 2 à 10ª potência.
(f) O valor absoluto da distância entre a altura de Sara (54 polegadas) e a altura de Mark (57 polegadas).
(g) O menor preço entre os seguintes preços: R$ 34,99, R$ 29,95 e R$ 31,50.
'''

#(a) A soma dos 5 primeiros inteiros positivos.
sum = 0
for i in range(1,11):
    if i%2==0:
        sum += i
        print(i)
print(sum)

#(b) A idade média de Sara (idade 23), Mark (idade 19) e Fátima (idade 31).
print((23+19+31)/3)

#(c) O número de vezes que 73 cabe em 403.
resultado = 403// 73
print(resultado)

#(d) O resto de quando 403 é dividido por 73
resultado = 403%73
print(resultado)

#(e) 2 à 10ª potência.
print(2**10)

#(f) O valor absoluto da distância entre a altura de Sara (54 polegadas) e a altura de Mark (57 polegadas).
print(57-54)

#(g) O menor preço entre os seguintes preços: R$ 34,99, R$ 29,95 e R$ 31,50.
a = 34.99
b = 29.95
c = 31;50
if a < b and a < c:
    print(a)
elif b < a and b < c:
    print(b)
else:
    print(c)

