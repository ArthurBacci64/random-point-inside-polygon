import random
from utilidades import *

poligono = Poligono(
    [ Ponto(0, 0)
    , Ponto(0.4, 0.1)
    , Ponto(1, 0.2)
    , Ponto(0, 1)
    ])

minx = min(map( lambda p: p.x , poligono.pontos ))
miny = min(map( lambda p: p.y , poligono.pontos ))
maxx = max(map( lambda p: p.x , poligono.pontos ))
maxy = max(map( lambda p: p.y , poligono.pontos ))

ponto_dentro = 0
tentativas = 0

while (ponto_dentro == 0):
    ponto = Ponto( random.uniform(minx, maxx)
                 , random.uniform(miny, maxy) )
    
    ponto_dentro = ponto_dentro_de_poligono(ponto, poligono)
    tentativas += 1

print("Ponto:", ponto)
print("Foram feitas {} tentativas".format(tentativas))

