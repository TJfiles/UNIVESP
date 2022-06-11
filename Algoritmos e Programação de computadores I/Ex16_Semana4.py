'''
Implemente a função trocaPU(), que aceita uma lista como entrada e troca o primeiro e último elementos da lista.
Você pode considerar que a lista não estará vazia. A função não deverá retornar nada.
 >>> ingredientes = ['farinha','açúcar','manteiga','maçãs']
>>> trocaPU(ingredientes)
>>> ingredientes
['maçãs','açúcar','manteiga','farinha']
'''
def trocaPU(list=list):
    intermed1 = list.pop(0)
    intermed2 = list.pop(-1)
    list.insert(0, intermed2)
    list.append(intermed1)
    print(list)

print(trocaPU(['maçãs','açúcar','manteiga','farinha']))
