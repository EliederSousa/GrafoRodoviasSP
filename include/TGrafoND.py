"""
Projeto da disciplina de Teoria dos Grafos

José Eduardo Bernardino Jorge   42019877
Elieder Damasceno Sousa         32093659

"""
import math
from include.fila import FilaCircular

# Define uma constante que guarda o maior valor suportado pela linguagem.
# Arestas que não existem terão este valor na matriz de adjacência.
INFINITO = math.inf
# Quantidade de vértices máxima default
TAM_MAX_DEFAULT = 1000  

# Classe disponibilizada no projeto.
class TGrafoND:
  # construtor da classe grafo
  def __init__(self, n=TAM_MAX_DEFAULT):
    self.n = n  # número de vértices
    self.m = 0  # número de arestas
    # matriz de adjacência
    self.adj = [[INFINITO for i in range(n)] for j in range(n)]
    self.nomes = []
    self.populacoes = []
    self.posicoes = []


  # Calcula qual é o grau de entrada do vértice
  def inDegree(self, v):
    degree = 0
    for i in range(self.n):
      if self.adj[i][v] != INFINITO:
        degree += 1
    return degree

  # Calcula o grau de saída do vértice
  def outDegree(self, v):
    degree = 0
    for i in range(self.n):
      if self.adj[v][i] != INFINITO:
        degree += 1
    return degree

  # Remove um vértice do grafo pelo nome
  def removeV(self, v):
    try:
      index = self.nomes.index(v)
      del self.nomes[index]
      del self.populacoes[index]
      del self.posicoes[index]
      # deleta as arestas relacionadas
      for w in range(self.n):
        if self.adj[w][index] != INFINITO:
          self.m -= 1
        del self.adj[w][index]
      # deleta o vértice
      del self.adj[index]
      self.n -= 1
      return True
    except ValueError:
      return False

  # Insere um vértice no grafo
  def insereV(self, nome, populacao, latitude, longitude):
    if self.n < TAM_MAX_DEFAULT:
      self.nomes.append(nome.upper())
      self.populacoes.append(populacao)
      self.posicoes.append([latitude, longitude])
      
      for w in range(len(self.adj)):
        self.adj[w].append(INFINITO)

      listaTemp = []
      for w in range(len(self.adj) + 1):
        listaTemp.append(INFINITO)

      self.adj.append(listaTemp)
      self.n += 1
      return True
    else:
      return False

  # Verifica se o grafo é simétrico
  @staticmethod
  def isSimetrico(g):
    for i in range(g.n):
      for w in range(g.n):
        if g.adj[i][w] != g.adj[w][i]:
          return 0
    return 1

  # Insere uma aresta v->w com peso
  def insereA(self, v, w, peso=1):
    try:
      indexV = self.nomes.index(v)
      indexW = self.nomes.index(w)
      if self.adj[indexV][indexW] == INFINITO:
        self.adj[indexV][indexW] = peso
        self.adj[indexW][indexV] = peso
        self.m += 1  # atualiza qtd arestas
      return True
    except ValueError:
      return False

  # Remove uma aresta v->w do Grafo
  def removeA(self, v, w):
    try:
      indexV = self.nomes.index(v)
      indexW = self.nomes.index(w)
      if self.adj[indexV][indexW] != INFINITO:
        self.adj[indexV][indexW] = INFINITO
        self.adj[indexW][indexV] = INFINITO
        self.m -= 1  # atualiza qtd arestas
      return True
    except ValueError:
      return False

  # Retorna uma lista com os vértices adjacentes a V
  def adjacencias(self, v):
    edges = []
    for index, edge in enumerate(self.adj[v]):
      if edge != INFINITO:
        edges.append(index)
    return edges

  # Breadth-first search  
  def percursoLargura( self, vInicial ):
    visitados = []
    me_visite = FilaCircular()
    visitados.append( vInicial )
    me_visite.enqueue( vInicial )
    while not me_visite.isEmpty():
      nova_casa = me_visite.dequeue()
      vizinhos_nao_visitados = [x for x in self.adjacencias( nova_casa ) if x not in visitados]
      while len( vizinhos_nao_visitados ) > 0:
        me_visite.enqueue( vizinhos_nao_visitados[0] )
        visitados.append( vizinhos_nao_visitados[0] )
        vizinhos_nao_visitados = [x for x in self.adjacencias( nova_casa ) if x not in visitados]
    return len(visitados) == self.n

  
  # Algoritmo de Dijsktra
  def dijkstra(self, vInicial, vFinal):
    try:
      indexV = self.nomes.index(vInicial)
      indexW = self.nomes.index(vFinal)
    except ValueError:
      return False
      
    distancias = [INFINITO] * self.n
    distancias[indexV] = 0
    A = [w for w in range(0, self.n)]
    S = [indexV]
    F = []
    k = 0
    rot = [-1 for w in range(0, self.n)]

    while len(A) > 0:
      k += 1
      distancias_de_A = []
      indexes = []
      for w in A:
        distancias_de_A.append(distancias[w])
        indexes.append(w)
      r = indexes[distancias_de_A.index(min(distancias_de_A))]
      F.append(r)
      A.remove(r)
      S = list(set(A) & set(self.adjacencias(r)))
      for i in S:
        p = min(distancias[i], distancias[r] + self.adj[r][i])
        if p < distancias[i]:
          distancias[i] = p
          rot[i] = r

    print("\n================================\n")
    print("A melhor rota entre {} e {} tem {:.1f}Km:\n".format(vInicial, vFinal, distancias[indexW]))
    rotas = []
    while indexW != indexV:
      rotas.append([self.nomes[indexW], distancias[indexW]])
      indexW = rot[indexW]

    print(self.nomes[indexV], end="")
    temp_dist = 0
    for w in range(len(rotas)-1, -1, -1):
      print( " {:.1f}Km → {}".format(rotas[w][1] - temp_dist, rotas[w][0]), end="" )
      temp_dist = rotas[w][1]
    print("\n\n================================\n")
    

  # Apresenta o Grafo contendo número de vértices, arestas (apenas as que existem) e a matriz de adjacência obtida
  def show(self):
    print(f"\n n: {self.n:2d} ", end="")
    print(f"m: {self.m:2d}\n")
    for i in range(self.n):
      for w in range(self.n):
        if self.adj[i][w] != INFINITO:
          print("adj[{},{}] = {} ".format(self.nomes[i], self.nomes[w], self.adj[i][w]))
      print("\n")
    print("\nFim da impressao do grafo.")