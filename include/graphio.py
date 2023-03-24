"""
Projeto da disciplina de Teoria dos Grafos

José Eduardo Bernardino Jorge   42019877
Elieder Damasceno Sousa         32093659

"""
import math
from unidecode import unidecode # tratamento de acento 

# Classe usada para gravar as informações nos arquivos de saída.
class GraphIO:
  def __init__(self, url, vertices, edges):
    #dummy constructor
    pass

  # Grava o arquivo grafo.txt. 
  @staticmethod
  def writeFile( url, vertices, totalEdges ):
    grafoout = "2\n"                               # Tipo de grafo: 2 (ñ direcionado, peso em arestas)
    grafoout += str( len(vertices) ) + "\n"        # Quantidade de vértices
    
    for w in range( len(vertices) ):               # Lista de vértices
      # unidecode() remove todos os acentos das letras. 
      grafoout += str(w) + " " + unidecode(vertices[w].name.upper()) + "\n"
    
    grafoout += str(totalEdges) + "\n"             # Total de arestas
  
    for w in range ( len(vertices) ) :             # Para cada vértice
      for k in range( len(vertices[w].edges ) ):   # E para cada aresta
        # Extrai a informação da origem/destino/peso de cada aresta. O peso é arredondado para 1 casa decimal.
        grafoout += str(vertices[w].edges[k].fromv) + " " + str(vertices[w].edges[k].to) + " " + str(str( math.floor( vertices[w].edges[k].weight * 10 ) / 10 )) + "\n"
  
    file = open( url, 'w' )
    file.write( grafoout )
    file.close()

  # Grava o arquivo grafo.graphml (GraphOnline)
  @staticmethod
  def writeXML( url, vertices, totalEdges ):
    grafoout =  "<?xml version=\"1.0\" encoding=\"UTF-8\"?><graphml><graph id=\"Graph\" uidGraph=\"3\" uidEdge=\""

    grafoout += str(totalEdges) + "\">"
    # Grava as informações dos vértices
    # 2000 é o ZOOMLEVEL. Veja a seção Apendice da documentação para ver exemplos de saída.
    for w in range( len( vertices ) ):
      grafoout += vertices[w].generateXMLNode( 2000 )
      
    # Grava as informações das arestas
    # Para cada vértice
    for w in range ( len(vertices) ) :        
      # E para cada aresta
      for k in range( len(vertices[w].edges ) ):
        grafoout += vertices[w].edges[k].generateXMLNode()
   
    grafoout += "</graph></graphml>"
    
    file = open( url, 'w' )
    file.write( grafoout )
    file.close()