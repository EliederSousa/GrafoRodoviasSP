"""
Projeto da disciplina de Teoria dos Grafos

José Eduardo Bernardino Jorge   42019877
Elieder Damasceno Sousa         32093659

"""
import math, os, re
from unidecode import unidecode
from include.TGrafoND import TGrafoND
from include.graphio import GraphIO
from include.vertice import Vertice
from include.edge import Edge
from include.point import Point

grafo = 0

# Lê o arquivo passado como parâmetro e cria o grafo correspondente.
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
    elif (lineNum > 1) and (lineNum < (tamanho + 2)):
      info = re.search("([^ ]*) ([^\d]*) ([^ ]*) ([^ ]*) (.*)", line)
      grafo.nomes.append(info[2])
      grafo.populacoes.append(int(info[3]))
      grafo.posicoes.append([float(info[4]), float(info[5])])
    elif lineNum > (tamanho + 2):
      info = re.search("([^ ]*) ([^ ]*) (.*)", line)
      indexcidade1 = int(info[1])
      indexcidade2 = int(info[2])
      grafo.insereA(grafo.nomes[indexcidade1], grafo.nomes[indexcidade2],
                    float(info[3]))


# Grava o grafo em um arquivo
def gravarDados(url):
  vert = []
  for w in range(grafo.n):
    vert.append(
      Vertice(grafo.nomes[w], w,
              Point(grafo.posicoes[w][0], grafo.posicoes[w][1]),
              grafo.populacoes[w]))

  counter = 0
  for x in range(grafo.n):
    for y in range(x + 1, grafo.n):
      if grafo.adj[x][y] != math.inf:
        vert[x].edges.append(Edge(x, y, grafo.adj[x][y], counter))
      counter += 1

  GraphIO.writeFile(url, vert, grafo.m)
  GraphIO.writeXML("output/grafo.graphml", vert, grafo.m)


# Limpa o console
def clearConsole():
  os.system('cls' if os.name == 'nt' else 'clear')


# Imprime o menu de opções.
def menu():
  global grafo
  print("+---------------------------------+")
  print("| GRAFO DAS RODOVIAS DE SÃO PAULO |")
  print("+---------------------------------+")
  print("| 1: Ler dados do arquivo.        |")
  print("| 2: Gravar os dados no arquivo.  |")
  print("| 3: Inserir vértice.             |")
  print("| 4: Inserir aresta.              |")
  print("| 5: Remover vértice.             |")
  print("| 6: Remover aresta.              |")
  print("| 7: Mostrar conteúdo do arquivo. |")
  print("| 8: Mostrar grafo.               |")
  print("| 9: Mostrar conexidade.          |")
  print("| 10: Objetivos do ODS.           |")
  print("| 11: Ver o melhor caminho.       |")
  print("| 12: Encerrar a aplicação.       |")
  print("+---------------------------------+\n")
  return int(input("Selecione uma opção acima: "))


# Loop principal
running = True
while running:
  escolha = menu()
  clearConsole()
  if escolha == 1:
    createGraphFromFile("output/grafo.txt")
    print("Grafo lido com sucesso.\n")
    print("Há um total de {} cidades.\n".format(grafo.n))
  elif escolha == 2:
    gravarDados("output/grafo.txt")
    print("Dados gravados com sucesso.\n")
  elif escolha == 3:
    nome = unidecode(input("Digite o nome da nova cidade: ").upper())
    populacao = int(input("Digite a populacao da nova cidade: "))
    latitude = float(input("Digite a latitude da cidade: "))
    longitude = float(input("Digite a longitude da cidade: "))
    if grafo.insereV(nome, populacao, latitude, longitude):
      print("Vertice inserido.\n")
    else:
      print("Erro ao inserir vertice.\n")
  elif escolha == 4:
    origem = unidecode(input("Digite a cidade de origem [ex: SAO PAULO]: ").upper())
    destino = unidecode(input("Digite a cidade de destino [ex: MOGI DAS CRUZES]: ").upper())
    peso = float(input("Digite o peso [ex: 10.0]: "))
    if peso > 0:
      if grafo.insereA(origem, destino, peso):
        print("Aresta criada.\n")
      else:
        print("Não foi possível criar a aresta.\n")
    else:
      print("Não foi possível criar a aresta, peso inválido.\n")
  elif escolha == 5:
    nome = unidecode(input("Digite o vertice para ser removido: ").upper())
    if grafo.removeV(nome):
      print("Vertice removido.\n")
    else:
      print("Erro ao remover vertice.\n")
  elif escolha == 6:
    origem = unidecode(input("Digite a cidade de origem: ").upper())
    destino = unidecode(input("Digite a cidade de destino: ").upper())
    if grafo.removeA(origem, destino):
      print("Aresta removida.\n")
    else:
      print("Não foi possível remover a aresta.\n")
  elif escolha == 7:
    file = open("output/grafo.txt", "r")
    for lineNum, line in enumerate(file):
      print(line, sep="")
  elif escolha == 8:
    grafo.show()
  elif escolha == 9:
    if grafo.percursoLargura(0) == 1:
      print("O grafo é não direcionado e conexo.\n")
    else:
      print("O grafo é não direcionado e desconexo.\n")
  elif escolha == 10:
    print("""
    Como parte do projeto, a aplicação mantém um conjunto de informações que visam mostrar quais indicadores da ODS são suplantados através da resolução de problemas de menor caminho.  

Analisando os indicadores, temos que o desenvolvimento de técnicas que visam dimensionar a malha rodoviária paulista constituem-se em soluções do objetivo 9: Indústria, Inovação e Infraestrutura - Construir infraestrutura resiliente, promover a industrialização inclusiva e sustentável, e fomentar a inovação.
Os tópicos desde objetivo visam apontar para questões de desenvolvimento na infraestrutura, o que se encaixa em um projeto de estudo de malhas rodoviárias; bem como o incentivo a pesquisa científica e o acesso a tecnologia são pontos que nossa aplicação tenta abordar ao dar ao usuário um sistema totalmente automatizado de cálculo de rotas. Alguns dos tópicos mais importantes deste objetivo que se encaixam na nossa solução, são:

9.1 - Desenvolver infraestrutura de qualidade, confiável, sustentável e resiliente, incluindo infraestrutura regional e transfronteiriça, para apoiar o desenvolvimento econômico e o bem-estar humano, com foco no acesso equitativo e a preços acessíveis para todos;
9.5 - Fortalecer a pesquisa científica, melhorar as capacidades tecnológicas de setores industriais em todos os países, particularmente nos países em desenvolvimento, inclusive, até 2030, incentivando a inovação e aumentando substancialmente o número de trabalhadores de pesquisa e desenvolvimento por milhão de pessoas e os gastos público e privado em pesquisa e desenvolvimento;
9.b - Apoiar o desenvolvimento tecnológico, a pesquisa e a inovação nacionais nos países em desenvolvimento, inclusive garantindo um ambiente político propício para, entre outras coisas, diversificação industrial e agregação de valor às commodities;
9.c - Aumentar significativamente o acesso às tecnologias de informação e comunicação e empenhar-se para procurar ao máximo oferecer acesso universal e a preços acessíveis à internet nos países menos desenvolvidos, até 2020.\n""")
    pass
  elif escolha == 11:
    origem = unidecode(input("Digite a cidade de origem [ex: SAO PAULO]: ").upper())
    destino = unidecode(input("Digite a cidade de destino [ex: MOGI DAS CRUZES]: ").upper())
    grafo.dijkstra( origem, destino )
  if escolha == 12:
    running = False

print("Encerrando a aplicação...")
