"""
Projeto da disciplina de Teoria dos Grafos

José Eduardo Bernardino Jorge   42019877
Elieder Damasceno Sousa         32093659

"""
import pandas, math
from include.graphio import GraphIO
from include.point import Point
from include.edge  import Edge
from include.vertice import Vertice

# https://stackoverflow.com/a/21623206
# Fórmula de Haversine
def distance( v1, v2 ):
  p = 0.017453292519943295
  a = 0.5 - math.cos((v2.position.x - v1.position.x) * p) / 2 + math.cos(v1.position.x * p) * math.cos(v2.position.x * p) * (1 - math.cos((v2.position.y - v1.position.y) * p)) / 2;
  return 12742 * math.asin(math.sqrt(a));

# Variáveis de controle para personalização do grafo.
MINPOPULATION = 0
ZOOMLEVEL = 2000

cidades = []
distancias = []
numEdges = 10000
totalEdges = 0

# Lendo o arquivo CSV.
df = pandas.read_csv('assets/data.csv', sep=";")

# Criando os vértices (cidades), de acordo com a população mínima
for w in range( len(df.index) ):
  if df['Populacao'].iloc[w] > MINPOPULATION :
    cidades.append( Vertice( df['Nome'].iloc[w], len(cidades), Point( df['Latitude'].iloc[w], df['Longitude'].iloc[w]), df['Populacao'].iloc[w] ))

print( "Total de cidades com menos de {} habitantes: {}".format( MINPOPULATION, len(cidades) ) )

totalValues = len(cidades)

# Para cada cidade...
for w in range( totalValues ):
  distancias = []
  # Cria arestas para todas as outras cidades.
  for j in range( totalValues ):
    # Evita criar arestas para o próprio vértice.
    if w != j:
      # Cria a aresta
      distancias.append( Edge(w, j, distance(cidades[w], cidades[j]), numEdges))
      numEdges += 1

  # Ordena as arestas por distância entre as cidades.
  distancias_copia = sorted(distancias, key=lambda edge: edge.weight)

  # Limita o número de arestas de cada cidade baseado em sua população.
  maxEdges = math.inf

  # Regras de criação de arestas. 
  if cidades[w].population < 20000:
    maxEdges = 1
  if cidades[w].population < 50000:
    maxEdges = 2
  elif cidades[w].population < 50000:
    maxEdges = 2
  elif cidades[w].population < 200000:
    maxEdges = 2
  elif cidades[w].population < 1000000:
    maxEdges = 4
  elif cidades[w].population < 5000000:
    maxEdges = 5
  else:
    maxEdges = 12

  # Adiciona as arestas no vértice (cidade)
  m = 0
  for k in range( len( distancias_copia ) ):
    if m < maxEdges:
      # Evita criar a aresta se ela já existir em sentido contrário. (grafo não orientado)
      if not cidades[distancias_copia[k].to].checkEdgeExists(distancias_copia[k].fromv):
        cidades[w].addEdge(distancias_copia[k])
        totalEdges += 1;
        m += 1

print( "Total de arestas:", totalEdges )

# Grava os arquivos para leitura no GraphOnline e o grafo.txt .
GraphIO.writeFile( "output/grafo.txt", cidades, totalEdges )
GraphIO.writeXML( "output/grafo.graphml", cidades, totalEdges )