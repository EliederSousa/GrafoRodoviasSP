"""
Projeto da disciplina de Teoria dos Grafos

José Eduardo Bernardino Jorge   42019877
Elieder Damasceno Sousa         32093659

"""
import math

# Classe utilizada para guardar as informações de uma aresta.
# Usada para facilitar a criação dos arquivos de saída
class Edge:
  def __init__(self, FROM_V, TO, WEIGHT, ID):
    self.fromv   = FROM_V
    self.to      = TO
    self.weight  = WEIGHT
    self.id      = ID

  # Retorna uma string com o conteúdo de um nó <edge> que é lido pelo XML do GraphOnline.
  def generateXMLNode( self ):
    text = "<edge source=\""
    text += str(self.fromv)
    text += "\" target=\""
    text += str(self.to)
    text += "\" isDirect=\"false\" weight=\""
    text += str( math.floor(self.weight * 10) /10 ) # Arredondamento em 1 casa decimal.
    text += "\" useWeight=\"true\" id=\""
    text += str(self.id)
    text += "\" text=\"\" upText=\"\" arrayStyleStart=\"\" arrayStyleFinish=\"\" ownStyles = \"{&quot;0&quot;:{&quot;baseStyles&quot;:[],&quot;strokeStyle&quot;:&quot;#000000&quot;,&quot;weightText&quot;:&quot;#464646&quot;,&quot;fillStyle&quot;:&quot;#7d95ca&quot;,&quot;textPadding&quot;:4,&quot;textStrokeWidth&quot;:2,&quot;lineDash&quot;:&quot;0&quot;,&quot;additionalTextColor&quot;:&quot;#ff8080&quot;,&quot;weightPosition&quot;:&quot;1&quot;}}\" model_width=\"3\" model_type=\"1\" model_curveValue=\"0\" ></edge>"
    return text