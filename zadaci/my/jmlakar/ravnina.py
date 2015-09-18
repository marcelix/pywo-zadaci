class Tocka:
    """
        Opis ove klase:)
        
        2-dim tocke u ravnini
    """
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def norm(self):
        return math.sqrt(self.x**2 + self.y**2)
      
    def __repr__(self):
        return "Tocka x={0}, y={1}".format(self.x,self.y)
    
class Vektor (Tocka):
    
    def __add__(self, b):
        return ((self.x + b.x), (self.y + b.y))
    
    def __sub__(self, b):
        return ((self.x - b.x), (self.y - b.y))
    
    def __mul__(self, n):
        return ((self.x * n), (self.y * n))
    
    def sc (self,b):
        return self.x * b.x + self.y * b.y
    
    def __repr__(self):
        return "Tocka x={0}, y={1}".format(self.x,self.y) 
    
''' 
a = Vektor(1,2)
b = Vektor(-12,34)

c = a * 2
print(c)

print (a.sc(b))   
'''