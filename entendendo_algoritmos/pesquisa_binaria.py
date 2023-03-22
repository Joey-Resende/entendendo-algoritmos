from rich import print
from time import sleep


def pesquisa_binaria(lista, item):
    baixo = 0
    alto = len(lista) - 1

    print('[bold yellow]*-*-' * 10)
    while baixo <= alto:
        meio = (baixo + alto) // 2
        print('>>> [bold blue]Verificando[/bold blue] o meio da lista...')
        sleep(0.5)
        chute = lista[meio]
        if chute == item:
            print('>>> [bold blue]Achou... [/bold blue]o item estava na posição', end=' ')
            sleep(0.5)
            return meio
        if chute > item:
            alto = meio - 1
            print(f'>>> O chute foi muito [bold magenta]alto!!![/bold magenta] = {meio}')
            sleep(0.5)
        else:
            baixo = meio + 1
            print(f'>>> O chute foi muito [bold magenta]baixo!!![/bold magenta] = {meio}')
            sleep(0.5)
    return print('>>> [bold red]Não foi encontrado!!!', end=' = ')


minha_lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(pesquisa_binaria(minha_lista, 3))
print(pesquisa_binaria(minha_lista, -1))
print(pesquisa_binaria(minha_lista, 8))

