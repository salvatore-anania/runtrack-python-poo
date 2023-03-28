class Personne:
    def __init__(self,age=14):
        self.__age=age

    def get_age(self):
        return self.__age
    
    def modifier_age(self,age):
        self.__age=age
    
    def afficher_age(self):
        print(self.__age)
        
    def bonjour(self):
        print("Hello")

class Eleve(Personne):
        
    def aller_en_cours(self):
        print("Je vais en cours")
        
    def affichage_age(self):
        print(f"J'ai {self.get_age()} ans.")

class Professeur(Personne):
    
    def __init__(self,age=14,matiere=""):
        super(age)
        self.matiere_enseignee=matiere
        
    def enseigner(self):
        print("Le cours vacommencer.")
        

        

moi=Personne()

eleve=Eleve()

eleve.affichage_age()
eleve.afficher_age()     