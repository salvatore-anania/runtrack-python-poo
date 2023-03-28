class Rectangle:
    def __init__(self,longueur=10,largeur=5):
        self.__longueur=longueur
        self.__largeur=largeur
    
    def get_longueur(self):
        return self.__longueur
    
    def get_largeur(self):
        return self.__largeur
    
    def set_longueur(self,longueur):
        self.__longueur=longueur
    
    def set_largeur(self,largeur):
        self.__largeur=largeur
        
    def perimetre(self):
        return (self.get_largeur()+self.get_longueur())*2
    
    def surface(self):
        return self.get_largeur()*self.get_longueur()

class Parallélépipède(Rectangle):
    
    def __init__(self,longueur,largeur,hauteur=0):
        super().__init__(longueur,largeur)
        self.__hauteur=hauteur
        
    def get_hauteur(self):
        return self.__hauteur
        
    def surface(self):
        return self.get_largeur()*self.get_longueur()*self.get_hauteur()
        
    
rectangle=Rectangle()

print(rectangle.get_largeur(),rectangle.get_longueur())
print(f"La longueur vaut {rectangle.get_largeur()} et la largeur vaut {rectangle.get_longueur()}.")
rectangle.set_largeur(20)
rectangle.set_longueur(10)
print(f"La longueur modifié vaut {rectangle.get_largeur()} et la largeur modifié vaut {rectangle.get_longueur()}.")

print(f"Le perimetre vaut {rectangle.perimetre()} et la surface vaut {rectangle.surface()}.")