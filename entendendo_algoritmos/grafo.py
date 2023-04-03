from collections import deque


def pessoa_e_vendedor(nome):
    return nome[-1] == 'm'


def pesquisa():
    fila_de_pesquisa = deque()
    fila_de_pesquisa += grafo[nome]
    verificadas = []
    while fila_de_pesquisa:
        pessoa = fila_de_pesquisa.popleft()
        if not pessoa in verificadas:
            if pessoa_e_vendedor(pessoa):
                print(f'{pessoa} é um vendedor de manga!')
                return True
            else:
                fila_de_pesquisa += grafo[pessoa]
                verificadas.append(pessoa)
    
    return False


pesquisa('voce')

