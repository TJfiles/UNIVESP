'''
Acrescente a docstring retorna a média de x e y à função média() e a docstring exibe os números
negativos contidos na lista lst à função negativos() dos Problemas Práticos 3.8 e 3.10.
Verifique seu trabalho usando a ferramenta de documentação help(). Você deverá receber, por exemplo:
'''

def negatives(list):
    '''Recebe uma lista e imprime os negativos desta lista'''
    for i in list:
        if i <0:
            print(i)

def media(x,y):
    '''Retorna a média de x e y'''
    media = (x+y)/2
    return media

print(help(negatives))
print(help(media))