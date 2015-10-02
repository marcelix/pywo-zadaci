"""
 Licenca, opis, itd.
"""

__author__ = "Ian Žonja"
__email__ = "ianzonja@foi.hr"

from math import sqrt


class Tocka:
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    
    def __repr__(self):
        return "Tocka({0}, {1})".format(self.x,self.y)
        

        
class Vektor(Tocka):
    
    def __add__(self, b):
        x = self.x + b.x
        y = self.y + b.y
        return Vektor(x, y)
    
    def __sub__(self,b):
        x = self.x - b.x
        y = self.y - b.y
        return Vektor(x,y)
    
    def __mul__(self,b):
        x = self.x * b
        y = self.y * b
        return Vektor(x,y)
    
    def norm(self):
        return sqrt( self.x**2 + self.y**2  )

    
    def __repr__(self):
        return "Vektor({0}, {1})".format(self.x,self.y)