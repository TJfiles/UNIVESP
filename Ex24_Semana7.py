'''
Usamos o padrão de laço aninhado para gerar todos os pares de índices de coluna e linha e somarmos as entradas correspondentes:
'''

def add2D(t1, t2):
    """t1 e t2 são listas 2D com o mesmo número de linhas e
    mesmo número de colunas de tamanho igual
    add2D incrementa cada item t1[i][j[ por t2[i][j]"""
    nlinhas = len(t1) # número de linhas
    ncolunas = len(t1[0]) # número de colunas
    for i in range(nlinhas): # para cada índice de linha i
        for j in range(ncolunas): # para cada índice de coluna j
            t1[i][j] += t2[i][j]
