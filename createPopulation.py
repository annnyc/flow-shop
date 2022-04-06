import numpy as np


def createPopulation(number_of_jobs: int, population_size: int):
    population = []

    for _ in range(population_size):

        novo_item = list(np.random.permutation(number_of_jobs))

        # incrementar 1, o np.random.permutation gera uma lista com os valores de 0 a n-1
        population.append([int(job + 1) for job in novo_item])

    return population
