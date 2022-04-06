import numpy as np
import time
import random
import sys

def criarPopulacaoInicial(Nm, Nj):
    pop = []
    for i in range(Nm):
        p = list(np.random.permutation(Nj))
        while p in pop:
            p = list(np.random.permutation(Nj))
        pop.append(p)

    return pop

def makespan(instancia, solucao):
    nM = len(instancia)
    tempo = [0] * nM
    tarefa = [0] * len(solucao)
    for t in solucao:
        if tarefa[t - 1] == 1:
            return "SOLUÇÃO INVÁLIDA: tarefa repetida!"
        else:
            tarefa[t - 1] = 1
        for m in range(nM):
            if tempo[m] < tempo[m - 1] and m != 0:
                tempo[m] = tempo[m - 1]
            tempo[m] += instancia[m][t - 1]
    return tempo[nM - 1]

def selecaoPais(pop, data):
    popObj = []
    for i in range(len(pop)):
        popObj.append([makespan(data, pop[i]), i])

    popObj.sort()
    # print(popObj)
    # sys.exit(0)

    distr = []
    distrInd = []

    for i in range(len(pop)):
        distrInd.append(popObj[i][1])
        prob = (2 * (i + 1)) / (len(pop) * (len(pop) + 1))
        distr.append(prob)

    parents = []
    for i in range(len(pop)):
        parents.append(list(np.random.choice(distrInd, 2, p=distr)))

    return parents


def crossover(parents, Nj):
    pos = list(np.random.permutation(np.arange(Nj - 1) + 1)[:2])

    if pos[0] > pos[1]:
        t = pos[0]
        pos[0] = pos[1]
        pos[1] = t

    child = list(parents[0])

    for i in range(pos[0], pos[1]):
        child[i] = -1

    p = -1
    for i in range(pos[0], pos[1]):
        while True:
            p = p + 1
            if parents[1][p] not in child:
                child[i] = parents[1][p]
                break

    return child

def mutation(sol, Nj):
    pos = list(np.random.permutation(np.arange(Nj))[:2])

    if pos[0] > pos[1]:
        t = pos[0]
        pos[0] = pos[1]
        pos[1] = t

    remJob = sol[pos[1]]

    for i in range(pos[1], pos[0], -1):
        sol[i] = sol[i - 1]

    sol[pos[0]] = remJob

    return sol

def elitismo(oldPop, newPop, data):
    bestSolInd = 0
    bestSol = makespan(data, oldPop[0])

    for i in range(1, len(oldPop)):
        tempObj = makespan(data, oldPop[i])
        if tempObj < bestSol:
            bestSol = tempObj
            bestSolInd = i

    rndInd = random.randint(0, len(newPop) - 1)

    newPop[rndInd] = oldPop[bestSolInd]

    return newPop

def findBestSolution(pop, data):
    bestSolInd = 0
    bestSol = makespan(data, pop[bestSolInd])
    for i in range(1, len(pop)):
        tempObj = makespan(data, pop[i])
        if tempObj < bestSol:
            bestSol = tempObj
            bestSolInd = i

    return bestSolInd, bestSol

def findWorstSolution(pop, data):
    worstSolInd = 0
    worstSol = makespan(data, pop[worstSolInd])
    for i in range(1, len(pop)):
        tempObj = makespan(data, pop[i])
        if worstSol < tempObj:
            worstSol = tempObj
            worstSolInd = i

    return worstSolInd, worstSol

if __name__ == '__main__':
    filename = "tai200_10.txt"
    f = open(filename, 'r')
    l = f.readline().split()

    # Quantidade de tarefas
    Nj = int(l[1])
    # Quantidade de máquinas
    Nm = int(l[0])

    # Probabilidade de mutação
    Pm = 0.05
    # Critério de parada (quantidade de gerações)
    stopGeneration = 50000
    # Critério de parada (tempo máximo de execução)
    stopTime = 20 * 60  # 20 minutos

    data = []

    # criação da estrutura do array
    for i in range(Nm):
        temp = []
        for j in range(Nj):
            temp.append(0)
        data.append(temp)

    # dados lidos do arquivo
    for i in range(Nm):
        line = f.readline().split()
        for j in range(int(len(line))):
            data[i][j] = int(line[j])

    f.close()
    # print(np.matrix(data))
    # sys.exit(0)
    # Start Timer
    t1 = time.time()

    # Criando a população inicial
    population = criarPopulacaoInicial(Nm, Nj)
    # print(np.matrix(population))
    # sys.exit(0)

    for i in range(stopGeneration):
        if ((time.time() - stopTime) >= t1):
            break

        # Selecionando os pais
        parents = selecaoPais(population, data)
        childs = []

        # Aplicação do crossover
        for p in parents:
            childs.append(crossover([population[p[0]], population[p[1]]], Nj))

        r = random.random()
        if r < Pm:  # Probalidade de mutação
            for c in childs:
                c = mutation(c, Nj)

        population = elitismo(population, childs, data)

t2 = time.time()

bestSolutionInd, bestSolutionTime = findBestSolution(population, data)
worstSolutionInd, worstSolutionTime = findWorstSolution(population, data)

print("Tempo de execução: %s" % (t2 - t1))
print("Melhor solução: %s" % population[bestSolutionInd])
print("Melhor tempo: %s " % bestSolutionTime)
print("")
print("Pior solução: %s" % population[worstSolutionInd])
print("Pior tempo: %s " % worstSolutionTime)
























