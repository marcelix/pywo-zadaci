
from math import sqrt

class Tocka:
    """
       Opis ove klase.
       
       2-dim tocke u ravnini.
    """
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def norm(self):
        return sqrt( self.x**2 + self.y**2  )
        
    
    def __repr__(self):
        return "Tocka({0}, {1})".format(self.x,self.y)
        

class Vektor(Tocka):

    def __add__(self, b):
        """ self je vektor, b je vektor
        """
        x = self.x + b.x
        y = self.y + b.y
        return Vektor(x, y)
    
    def __sub__(self, b):
        """ self je vektor, b je vektor
        """
        x = self.x - b.x
        y = self.y - b.y
        return Vektor(x, y)
    
    def __mul__(self, b):
        """ self je vektor, b je vektor
        """
        if (type(b)==int):
            x = self.x * b
            y = self.y * b
            return Vektor(x, y)
        else:
            return sum(p*q for p,q in zip([self.x,self.y], [b.x,b.y]))
        
    def __rmul__(self, b):
        """ self je vektor, b je vektor
        """
        if (type(b)==int):
            x = b * self.x
            y = b * self.y
            return Vektor(x, y)
        else:
            return sum(p*q for p,q in zip([self.x,self.y], [b.x,b.y]))
    
    def __repr__(self):
        return "Vektor({0}, {1})".format(self.x,self.y)