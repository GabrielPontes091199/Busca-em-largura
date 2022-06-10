from collections import defaultdict
import time
import timeit

class Graph:

    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def BFS(self, s):
        visited = [False] * (len(self.graph))
        queue = []
        queue.append(s)
        visited[s] = True

        while queue:
            s = queue.pop(0)
            print(s, " ")
            for i in self.graph[s]:
                # print(visited[i])
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True

# INICIO
tempo_i = timeit.default_timer()

g = Graph()

with open("grafoBfs40.txt", "r") as f:
    for line in f:
        u, v = map(int, line.split())
        g.addEdge(u, v)

print ("Execução da busca em largura, começando pelo vértice 1:")
g.BFS(3)
tempo_f = timeit.default_timer()
print("Tempo execução: {0}".format(str(tempo_f - tempo_i)))
