
#(x1,y1),(x2,y2),(x3.y3)
import math

class Punto:

    def __init__(self,x=0,y=0):
        self.x = x
        self.y = y

    def distancia(self,p):
        d = math.sqrt((p.x - self.x)**2 + (p.y -self.y)**2)
        return d


a = Punto(10,8)
b = Punto(9,3)
c = Punto(2,4)

def promedio(a,b,c):
    res = (a.distancia(b) + b.distancia(c) + c.distancia(a))/3
    return res


print(a.distancia(b))
print(b.distancia(c))
print(c.distancia(a))
print('------')

print(promedio(a,b,c))


print(promedio(a,b,c))


def IsPalindromo(palabra):
    reversa=''.join(reversed(palabra))
    if palabra == reversa:
        return True
    else:
        return False


print(IsPalindromo('menem'))
