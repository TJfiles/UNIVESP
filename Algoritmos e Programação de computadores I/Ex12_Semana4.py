'''
Implemente a função perímetro(), que aceita, como entrada, o raio de um círculo (um número não negativo) e retorna o
perímetro do círculo. Você deverá escrever sua implementação em um módulo chamado perímetro.py. Um exemplo de uso é:
 >>> perimeter(1)
 6.283185307179586
'''

import math
def perimeter(raio):
    perim = (math.pi*2)*raio
    return perim


