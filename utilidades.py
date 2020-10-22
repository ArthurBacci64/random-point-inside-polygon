# Código de https://rosettacode.org/wiki/Ray-casting_algorithm#Python
# Com algumas poucas modificações

class Ponto:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __repr__(self):
        return "({}, {})".format(self.x, self.y)

class Linha:
    def __init__(self, x0, y0, x1, y1):
        self.a = Ponto(x0, y0)
        self.b = Ponto(x1, y1)

    @classmethod
    def fromPoints(cls, a, b):
        self = cls(a.x, a.y, b.x, b.y)
        return self
        

class Poligono:
    def __init__(self, pontos):
        self.pontos = pontos
        self.linhas = []

        for i in range(len(self.pontos)):
            if (i < len(self.pontos) - 1):
                l = Linha.fromPoints(self.pontos[i], self.pontos[i+1])
            else:
                l = Linha.fromPoints(self.pontos[i], self.pontos[0])
            self.linhas.append(l)

def ponto_dentro_de_poligono(poli, pon):
    if (len(poli.pontos) < 3):
        return 0

    return 1



from collections import namedtuple
from pprint import pprint as pp
import sys
 
 
_eps = 0.00001
_huge = sys.float_info.max
_tiny = sys.float_info.min
 
def rayintersectseg(p, l):
    ''' takes a point p=Pt() and an edge of two endpoints a,b=Pt() of a line segment returns boolean
    '''
    a = l.a
    b = l.b
    if a.y > b.y:
        a, b = b, a
    if p.y == a.y or p.y == b.y:
        p = Pt(p.x, p.y + _eps)
 
    intersect = False
 
    if (p.y > b.y or p.y < a.y) or (
        p.x > max(a.x, b.x)):
        return False
 
    if p.x < min(a.x, b.x):
        intersect = True
    else:
        if abs(a.x - b.x) > _tiny:
            m_red = (b.y - a.y) / float(b.x - a.x)
        else:
            m_red = _huge
        if abs(a.x - p.x) > _tiny:
            m_blue = (p.y - a.y) / float(p.x - a.x)
        else:
            m_blue = _huge
        intersect = m_blue >= m_red
    return intersect
 
_odd = lambda x: x % 2 == 1
 
def ponto_dentro_de_poligono(p, poly):
    ln = len(poly.linhas)
    return _odd(sum( rayintersectseg(p, l) for l in poly.linhas ))
 
