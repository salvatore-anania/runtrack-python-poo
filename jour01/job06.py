class Rectangle:
    def __init__(self):
        self.longueur=10
        self.largeur=5
    
    def get_longueur(self):
        return self.longueur
    
    def get_largeur(self):
        return self.largeur
    
    def set_longueur(self,longueur):
        self.longueur=longueur
    
    def set_largeur(self,largeur):
        self.largeur=largeur
    
        
    
rectangle=Rectangle()



rectangle.set_largeur(20)
rectangle.set_longueur(10)
print(f"La longueur vaut {rectangle.get_longueur()} et la largeur vaut {rectangle.get_largeur()} .")