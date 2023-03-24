"""
Projeto da disciplina de Teoria dos Grafos

José Eduardo Bernardino Jorge   42019877
Elieder Damasceno Sousa         32093659

"""
import math

# Classe utilizada para guardar as informações de um vértice.
# Usada para facilitar a criação dos arquivos de saída.
class Vertice:
  def __init__(self, NAME, ID, POINT, POPULATION):
    self.name   = NAME
    self.id     = ID
    self.position = POINT
    self.population = POPULATION
    self.edges = []
    
  def addEdge(self, EDGE ):
    self.edges.append( EDGE )

  # Checa se uma aresta já existe partindo desta cidade para a cidade passada no argumento.
  def checkEdgeExists(self, TO ):
    for w in range( len(self.edges) ):
        if self.edges[w].to == TO:
            return True
    return False

  # Gera um nó XML para este vértice na escala ZOOMLEVEL.
  def generateXMLNode(self, ZOOMLEVEL=2000 ):
    text = "<node positionX=\""
    # Latitudes e Longitudes precisam ser traduzidas para um contexto de um plano cartesiano.
    # Logo, foi necessário uma certa manipulação dos valores, como abaixo.
    text += str(self.position.y * ZOOMLEVEL + (20 * ZOOMLEVEL))
    text += "\" positionY=\""
    text += str(-self.position.x * ZOOMLEVEL + (40 * ZOOMLEVEL))
    text += "\" id=\""
    text += str(self.id)
    text += "\" mainText=\""
    text += self.name
    text += '''" upText="" ownStyles = "{&quot;0&quot;:{&quot;baseStyles&quot;:[],&quot;lineWidth&quot;:3,&quot;strokeStyle&quot;:&quot;#000000&quot;,&quot;fillStyle&quot;:&quot;#65cf75&quot;,&quot;mainTextColor&quot;:&quot;#000000&quot;,&quot;shape&quot;:0,&quot;upTextColor&quot;:&quot;#68aeba&quot;,&quot;commonTextPosition&quot;:0}}" size="'''
    # O tamanho (visualmente falando) do vértice no grafo depende da população da cidade.
    if self.population < 100000:
        text += str(25)
    else:
        if self.population > 2000000:
            text += str(80)
        else:
            text += str(math.floor((25 + self.population / 50000)*10)/10)
    text += "\" ></node>"
    return text