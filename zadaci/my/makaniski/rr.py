import sys
from ravnina import Tocka,Vektor

L = str(sys.argv)
print(L)
if 'add' in L:
    K = [s for s in L if s.isdigit()]
    a = Vektor(int(K[0]),int(K[1]))
    b = Vektor(int(K[2]),int(K[3]))
    c = a + b
    print(c)
if 'sub' in L:
    K = [s for s in L if s.isdigit()]
    a = Vektor(int(K[0]),int(K[1]))
    b = Vektor(int(K[2]),int(K[3]))
    c = a - b
    print(c)
if 'mul' in L:
    K = [s for s in L if s.isdigit()]
    a = Vektor(int(K[0]),int(K[1]))
    b = Vektor(int(K[2]),int(K[3]))
    c = a * b
    print(c)
