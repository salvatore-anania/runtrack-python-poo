class Livre:
    def __init__(self):
        self.__titre="Titre"
        self.__auteur="auteur"
        self.__nombrepages=100
    
    def get_titre(self):
        return self.__titre
    
    def get_auteur(self):
        return self.__auteur
    
    def get_nombrepages(self):
        return self.__nombrepages
    
    def set_titre(self,titre):
        self.__titre=titre
    
    def set_auteur(self,auteur):
        self.__auteur=auteur
        
    def set_nombrepages(self,nombrepages):
        if nombrepages>0:
            self.__nombrepages=nombrepages
        else:
            print("Nombres de pages non valide entrez un nombre superieur à 0")
    
        
    
livre=Livre()




print(f"le titre du livre est {livre.get_titre()} et son auteur {livre.get_auteur()}, il contient {livre.get_nombrepages()} pages.")
livre.set_auteur("jules vernes")
livre.set_titre("Le tour du monde en 80 jours")
livre.set_nombrepages(-67)
livre.set_nombrepages(67)
print(f"le titre du livre est {livre.get_titre()} et son auteur {livre.get_auteur()}, il contient {livre.get_nombrepages()} pages.")