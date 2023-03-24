"""
Projeto da disciplina de Teoria dos Grafos

José Eduardo Bernardino Jorge   42019877
Elieder Damasceno Sousa         32093659

"""
import math, os, re
from include.TGrafoND import TGrafoND
from include.graphio import GraphIO
from include.vertice import Vertice
from include.edge import Edge

grafo = 0

# Cria o grafo contido no arquivo passado como parâmetro.
def createGraphFromFile(url):
  global grafo
  tamanho = 0
  file = open(url, "r")
  for lineNum, line in enumerate(file):
    # Cria o grafo com a quantidade de vértices da linha 1
    if lineNum == 1:
      grafo = TGrafoND(int(line))
      tamanho = int(line)
    # Insere cada um dos vértices
    elif (lineNum > 1) and (lineNum < (tamanho+2)):
      info = re.search("([^ ]*) (.*)", line)
      grafo.nomes.append(info[2])
    elif lineNum > (tamanho+2):
      info = re.search("([^ ]*) ([^ ]*) (.*)", line)
      indexcidade1 = int(info[1])
      indexcidade2 = int(info[2])
      grafo.insereA( grafo.nomes[indexcidade1], grafo.nomes[indexcidade2], float(info[3]) )


# Grava o grafo em um arquivo
def gravarDados( url ):
  vert = []
  for w in range( grafo.n ):
    vert.append( Vertice(grafo.nomes[w], w, 0, 0 ) )
      
  for x in range( grafo.n ):
    for y in range( x+1, grafo.n ):
      if grafo.adj[x][y] != math.inf:
        vert[x].edges.append( Edge(x, y, grafo.adj[x][y], 0) )
        
  GraphIO.writeFile( url, vert, grafo.m)

# Limpa o console
def clearConsole():
  os.system('cls' if os.name == 'nt' else 'clear')


# Imprime o menu de opções.
def menu():
  global grafo
  print("+---------------------------------+")
  print("| GRAFO DAS RODOVIAS DE SÃO PAULO |")
  print("+---------------------------------+")
  print("| 1: Ler dados do arquivo.        |") # OK
  print("| 2: Gravar os dados no arquivo.  |")
  print("| 3: Inserir vértice.             |") # OK
  print("| 4: Inserir aresta.              |") # OK
  print("| 5: Remover vértice.             |") # OK
  print("| 6: Remover aresta.              |") # OK
  print("| 7: Mostrar conteúdo do arquivo. |") # OK
  print("| 8: Mostrar grafo.               |") # OK
  print("| 9: Encerrar a aplicação.        |") # OK
  print("+---------------------------------+\n")
  return int(input("Selecione uma opção acima: "))



running = True
# Loop principal
while running:
  escolha = menu()
  clearConsole()  
  if escolha == 1:
    createGraphFromFile("output/grafo.txt")
    print("Grafo lido com sucesso.\n")
  elif escolha == 2:
    gravarDados("output/grafo.txt")
    print("Dados gravados com sucesso.\n")
  elif escolha == 3:
    nome = input("Digite o nome do novo vertice: ")
    if grafo.insereV(nome.upper()):
      print("Vertice inserido.\n")
    else:
      print("Erro ao inserir vertice.\n")
  elif escolha == 4:
    origem = input("Digite a cidade de origem [ex: SAO PAULO]: ")
    destino = input("Digite a cidade de destino [ex: MOGI DAS CRUZES]: ")
    peso = float(input("Digite o peso [ex: 10.0]: "))
    if peso > 0:
      if grafo.insereA(origem.upper(), destino.upper(), peso):
        print("Aresta criada.\n")
      else:
        print("Não foi possível criar a aresta.\n")
    else:
        print("Não foi possível criar a aresta, peso inválido.\n")
  elif escolha == 5:
    nome = input("Digite o vertice para ser removido: ")
    if grafo.removeV(nome.upper()):
      print("Vertice removido.\n")
    else:
      print("Erro ao remover vertice.\n")
  elif escolha == 6:
    origem = input("Digite a cidade de origem: ")
    destino = input("Digite a cidade de destino: ")
    if grafo.removeA(origem.upper(), destino.upper()):
      print("Aresta removida.\n")
    else:
      print("Não foi possível remover a aresta.\n")
  elif escolha == 7:
    file = open("output/grafo.txt", "r")
    for lineNum, line in enumerate(file):
      print(line, sep="")
  elif escolha == 8:
    grafo.show()
  if escolha == 9:
    running = False

print("Encerrando a aplicação...")
