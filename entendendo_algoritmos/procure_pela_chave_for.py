from rich import print


def procure_pela_chave(caixa):
    for item in caixa:
        if item.e_uma_caixa():
            procure_pela_chave(item)
        elif item.e_uma_chave():
            print('Achei a chave!')


procure_pela_chave('chave')

