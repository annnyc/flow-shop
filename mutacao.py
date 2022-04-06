import random
from tokenize import Floatnumber
from typing import List
import numpy as np


def realizar_mutacao(filho: List[int]) -> List[int]:
    pos = list(np.random.permutation(np.arange(len(filho)))[:2])

    if pos[0] > pos[1]:
        t = pos[0]
        pos[0] = pos[1]
        pos[1] = t

    remJob = filho[pos[1]]

    for i in range(pos[1], pos[0], -1):
        filho[i] = filho[i - 1]

    filho[pos[0]] = remJob

    return filho


def mutacao(populacao: List[List[int]], probabilidade_mutacao: Floatnumber) -> List[List[int]]:
    populacao_mutada = []

    for filho in populacao:
        if random.random() < probabilidade_mutacao:
            populacao_mutada.append(realizar_mutacao([*filho]))
        else:
            populacao_mutada.append([*filho])

    return populacao_mutada
