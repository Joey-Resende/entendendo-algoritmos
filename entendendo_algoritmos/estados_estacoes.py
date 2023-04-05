estados_abranger = set(['mt', 'wa', 'or', 'id', 'nv', 'ut', 'ca', 'az'])

estacoes = {}
estacoes['kum'] = set(['id', 'nv', 'ut'])
estacoes['kdois'] = set(['wa', 'id', 'mt'])
estacoes['ktres'] = set(['or', 'nv', 'ca'])
estacoes['kquatro'] = set(['nv', 'ut'])
estacoes['kcinco'] = set(['ca', 'az'])

estacoes_finais = set()

def minha_colecao_coberta(estados_abranger, estacoes):
    estacoes_finais = set()
    while estados_abranger:
        melhor_estacao = None
        estados_cobertos = set()
        for estacao, estados in estacoes.items():
            cobertos = estados_abranger & estados
            if len(cobertos) > len(estados_cobertos) and estacao not in estacoes_finais:
                melhor_estacao = estacao
                estados_cobertos = cobertos
        if melhor_estacao is not None:
            estados_abranger -= estados_cobertos
            estacoes_finais.add(melhor_estacao)
            estacoes.pop(melhor_estacao)
        else:
            return None
    return estacoes_finais

print(minha_colecao_coberta(estados_abranger, estacoes))
