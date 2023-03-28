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
    
rectangle=Rectangle()

print(f"L'aire du rectangle est {rectangle.aire()}.")