import math
import random
from typing import List, Tuple


def removerRepetidos(populacao, aptidaoPop) -> List[List[int]]:
    indices_para_remover = []

    for i in aptidaoPop:
        if i == "SOLUÇÃO INVÁLIDA: tarefa repetida!":
            indices_para_remover.append(aptidaoPop.index(i))

    nova_populacao = [populacao[i] for i in range(
        len(populacao)) if i not in indices_para_remover]
    nova_aptidaoPop = [aptidaoPop[i] for i in range(
        len(aptidaoPop)) if i not in indices_para_remover]

    return nova_populacao, nova_aptidaoPop


def selecionarPares(indices_para_selecionar: List[int]):
    items_selecionados = []

    queue = [*indices_para_selecionar]
  
    while len(queue) > 1:
        pai_1 = random.choice(queue)
        queue.remove(pai_1)

        pai_2 = random.choice(queue)
        queue.remove(pai_2)

        items_selecionados.append((pai_1, pai_2))
    
    return items_selecionados


## retorna pares de 1/4 dos melhores pais
def selecionarPop(populacao: List[List[int]], aptidaoPop: List[int], POPULATION_SIZE: int, TAXA_DA_PROXIMA_GERAÇÃO) -> List[Tuple[int, int]]:
    nova_populacao, nova_aptidao = removerRepetidos(populacao, aptidaoPop)

    aptidao_ordenada = sorted(nova_aptidao, reverse=True)

    # 1/4 dos melhores pais serão selecionados
    valores_das_melhores_solucoes = set(aptidao_ordenada[POPULATION_SIZE // math.floor(TAXA_DA_PROXIMA_GERAÇÃO):])

    # indices das melhores solucoes
    indices_das_melhores_solucoes = []

    for i in range(len(nova_aptidao)):
        if nova_aptidao[i] in valores_das_melhores_solucoes:
            indices_das_melhores_solucoes.append(i)

    indices_dos_pares = selecionarPares(indices_das_melhores_solucoes)

    # melhores solucoes em população
    # selecionar os melhores pais
    melhores_pais = []

    for (pai1_indice, pai2_indice) in indices_dos_pares:
        melhores_pais.append((nova_populacao[pai1_indice], nova_populacao[pai2_indice]))

    return melhores_pais
