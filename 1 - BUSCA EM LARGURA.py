import time
import timeit

#importa a biblioteca para poder criar uma lista
from collections import defaultdict 
 
#classe para criação do grafo direcionado e que usa representação de lista de adjacência
class Graph: 
 
    #constroi a função que ira criar a lista 
   def __init__(self): 
 
        #Quando você cria um defaultdict, fornece uma função usada para criar valores, nesse caso criou-se a lista
        self.graph = defaultdict(list) 
 
    #Função que adiciona os vértices no grafo, relacionando os vertices que tem uma aresta entre si
   def addEdge(self,u,v): 
        self.graph[u].append(v) 
 
    #função para imprimir a BFS do grafo, recebe o primeiro nó a ser visitado 
   def BFS(self, s): 
 
        #marca todos os vértices como não visitados.
      visited = [False] * (len(self.graph)) 
      
        #cria uma fila vazia para o BFS 
      queue = [] 
 
        #pega o nó de origem, marca como visitado e insere ele na fila
      queue.append(s) 
      visited[s] = True
 
      #enquanto a fila não for vazia
      while queue: 
 
            #retira o último vértice inserido na fila e imprime
         s = queue.pop(0) 
         print(s, " ") 
 
            #Obtenha todos os vértices adjacentes dos vértices desenfileirados. Se um adjacente não foi visitado, marque-o como visitado e coloque-o na fila
         for i in self.graph[s]: 
            #print(visited[i])
            if visited[i] == False: 
               queue.append(i) 
               visited[i] = True
 

tempo_i = timeit.default_timer() 
# Criação do grafo
g = Graph() 
g.addEdge(0, 2) 
g.addEdge(0, 4) 
g.addEdge(0, 3)
g.addEdge(1, 4)
g.addEdge(1, 2) 
g.addEdge(2, 4) 
g.addEdge(3, 4) 
g.addEdge(3, 5)
g.addEdge(4, 5)
g.addEdge(5, 1)
g.addEdge(2, 6)
g.addEdge(6, 3) 
 
print ("Execução da busca em largura, começando pelo vértice 3:")
g.BFS(1) 

tempo_f = timeit.default_timer()
print("Tempo execução: {0}".format(str(tempo_f - tempo_i)))