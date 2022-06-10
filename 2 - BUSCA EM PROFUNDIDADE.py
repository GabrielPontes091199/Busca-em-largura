import time
import timeit

tempo_i = timeit.default_timer() 
grafo = {
    'a': ['b', 'd', 'e'],
    'b': ['a', 'c', 'e'],
    'c': ['b', 'e'],
    'd': ['a', 'e'],
    'e': ['a', 'b', 'c', 'd', 'f'],
    'f': ['e']
}

valor_profundidade_entrada = 0
valor_profundidade_saida = 0
profundidades_entrada_saida = {}
pai = {}
aresta = {}
niveis = {}
low = {}
demarcadores = set()
articulacoes = set()


def busca_em_profundidade(grafo, vertice_do_grafo):
    for vertice in grafo:
        low[vertice] = vertice

    pai[vertice_do_grafo] = None
    qtd_filhos_da_raiz = call_to_busca_em_profundidade(grafo, vertice_do_grafo, 1)
    if qtd_filhos_da_raiz <= 1:
        articulacoes.remove(vertice_do_grafo)


def call_to_busca_em_profundidade(grafo, vertice_do_grafo, nivel):
    global valor_profundidade_entrada, valor_profundidade_saida
    valor_profundidade_entrada += 1
    profundidades_entrada_saida[vertice_do_grafo] = [valor_profundidade_entrada, None]
    niveis[vertice_do_grafo] = nivel
    count_filhos = 0

    for vizinho in grafo.get(vertice_do_grafo):
        print('%s -> %s:' % (str(vertice_do_grafo), str(vizinho)))
        if not profundidades_entrada_saida.get(vizinho):
            pai[vizinho] = vertice_do_grafo
            count_filhos += 1
            aresta[(vertice_do_grafo, vizinho)] = 'aresta de arvore'
            print('aresta de arvore')
            call_to_busca_em_profundidade(grafo, vizinho, nivel + 1)

            if niveis[low[vizinho]] < niveis[low[vertice_do_grafo]]:
                low[vertice_do_grafo] = low[vizinho]

            if vizinho in demarcadores:
                articulacoes.add(
                    vertice_do_grafo)
        else:
            if not profundidades_entrada_saida[vizinho][1]:
                if pai[
                    vertice_do_grafo] != vizinho:
                    aresta[(vertice_do_grafo, vizinho)] = 'aresta de retorno'
                    print('aresta de retorno')
                    if niveis[vizinho] < niveis[low[vertice_do_grafo]]:
                        low[vertice_do_grafo] = vizinho
                else:
                    aresta[(vertice_do_grafo, vizinho)] = 'aresta de arvore'
                    print('aresta de arvore')
            else:
                aresta[(vertice_do_grafo, vizinho)] = 'aresta de arvore'
                print('aresta de arvore')

    valor_profundidade_saida += 1
    profundidades_entrada_saida[vertice_do_grafo][1] = valor_profundidade_saida

    if low[vertice_do_grafo] in (vertice_do_grafo, pai[vertice_do_grafo]):
        demarcadores.add(vertice_do_grafo)

    return count_filhos

busca_em_profundidade(grafo, 'a')
tempo_f = timeit.default_timer()
print("Tempo execução: {0}".format(str(tempo_f - tempo_i)))