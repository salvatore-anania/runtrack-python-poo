class Livre:
    def __init__(self):
        self.__titre="Titre"
        self.__auteur="auteur"
        self.__nombrepages=100
        self.__disponible=True
    
    def get_titre(self):
        return self.__titre
    
    def get_auteur(self):
        return self.__auteur
    
    def get_nombrepages(self):
        return self.__nombrepages
    
    def get_dipsponible(self):
        if self.__disponible:
            return "disponible"
        else:
            return "non disponible"
    
    def set_titre(self,titre):
        self.__titre=titre
    
    def set_auteur(self,auteur):
        self.__auteur=auteur
        
    def set_nombrepages(self,nombrepages):
        if nombrepages>0:
            self.__nombrepages=nombrepages
        else:
            print("Nombres de pages non valide entrez un nombre superieur à 0")
    
    def verification(self):
        if self.__disponible:
            return True
        else:
            return False
        
    def emprunter(self):
        if self.verification():
            self.__disponible=False
            
    def rendre(self):
        if not self.verification():
            self.__disponible=True
    
livre=Livre()

print(f"Le livre est {livre.get_dipsponible()}.")
livre.emprunter()
print(f"Le livre est {livre.get_dipsponible()}.")
livre. rendre()
print(f"Le livre est {livre.get_dipsponible()}.")