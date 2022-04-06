def retornaMelhorSolucao(populacao, aptidaoPop):
    smaller_index = 0
    smaller_value = aptidaoPop[0]

    for index in range(len(aptidaoPop)):
        solucao = aptidaoPop[index]

        if solucao == "SOLUÇÃO INVÁLIDA: tarefa repetida!":
            continue

        if solucao < smaller_value:
            smaller_value = solucao
            smaller_index = index

    return {
        "aptidao": smaller_value,
        "solucao": populacao[smaller_index]
    }
