import math

class Forme:
    def __init__(self):
        pass
    
    def aire(self):
        return 0
    
class Rectangle(Forme):
    
    def __init__(self,largeur=5,hauteur=8):
        self.__largeur=largeur
        self.__hauteur=hauteur
        
    def get_largeur(self):
        return self.__largeur
    
    def get_hauteur(self):
        return self.__hauteur
        
    def aire(self):
        return self.get_largeur()*self.get_hauteur()
    
class Cercle(Forme):
    
    def __init__(self,radius=5):
        self.__radius=radius
        
    def get_radius(self):
        return self.__radius
    
    def get_hauteur(self):
        return self.__hauteur
        
    def aire(self):
        return self.get_radius()*self.get_radius()*math.pi
    
cercle=Cercle()
rectangle=Rectangle()

print(f"L'aire du rectangle est {rectangle.aire()} et celle du cercle est {cercle.aire()}.")