"""
Projeto da disciplina de Teoria dos Grafos

José Eduardo Bernardino Jorge   42019877
Elieder Damasceno Sousa         32093659

"""
import math

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
  def insereV(self, v):
    if self.n < TAM_MAX_DEFAULT:
      self.nomes.append(v.upper())
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