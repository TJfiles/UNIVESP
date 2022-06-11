'''3.15 A solução usa as funções jump() do módulo turtlefunctions que desenvolvemos no estudo de caso. Para que o Python
 importe esse módulo, ele precisa estar na mesma pasta do módulo que contém a função olimpíadas().'''

'''import turtlefunctions

def olimpíadas(t):

    'faz tartaruga t desenhar os anéis olímpicos'

    t.pensize(3)

    jump(t, 0, 0) # fundo do círculo superior central

    t.setheading(0)

    t.circle(100) # círculo superior central

    turtlefunctions.jump(t, -220, 0)

    t.circle(100) # círculo superior esquerdo

    turtlefunctions.jump(t, 220, 0)

    t.circle(100) # círculo superior direito

    turtlefunctions.jump(t, 110, -100)

    t.circle(100) # círculo inferior direito

    turtlefunctions.jump(t, -110, -100)

    t.circle(100) # círculo inferior esquerdo'''