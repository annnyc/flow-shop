import json
import random
from typing import List, Tuple

'''
  1/4 dos individuos são os pais da geração passada
  Retornar os melhores indivíduos da geração passada (pais)
  e aleatoriamente os individuos da geração passada
'''


def selecionarNovaGeracao(melhores_da_geracao_passada: List[Tuple[int, int]], nova_geracao: List[List[int]], tamanho_populacao: int) -> List[List[int]]:
    geracao_passada_lista = []
    nova_geracao_copia = [item for sublist in nova_geracao for item in sublist]

    for item in melhores_da_geracao_passada:
        geracao_passada_lista.append(item[0])
        geracao_passada_lista.append(item[1])

    # Selecionar aleatoriamente os filhos da nova geração
    nova_geracao_lista = []

    for _ in range(tamanho_populacao - len(geracao_passada_lista)):
        item = random.choice(nova_geracao_copia)
        nova_geracao_lista.append(item)

        nova_geracao_copia.remove(item)

    nova_geracao_para_retornar = [*nova_geracao_lista, *geracao_passada_lista]

    elementos = list(set(json.dumps(x) for x in nova_geracao_para_retornar))
    elementos_unicos = [json.loads(x) for x in elementos]

    # possivelmente existem duplicatas, remover elas e adicionar novos items aleatorios
    while len(elementos_unicos) != tamanho_populacao and len(nova_geracao_copia) > 0:
        try:
            possivel_filho = random.choice(nova_geracao_copia)
            possivel_filho_string = json.dumps(possivel_filho)
        except Exception as e:
            print(nova_geracao_copia)
            return
        elementos_unicos_set = set([json.dumps(i)
                                   for i in nova_geracao_para_retornar])

        if possivel_filho_string in elementos_unicos_set:
            nova_geracao_copia.remove(possivel_filho)
            continue

        nova_geracao_copia.remove(possivel_filho)

        elementos_unicos.append(possivel_filho)

    return elementos_unicos

