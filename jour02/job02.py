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
    
    def __init__(self,age=14,matiere="Algorithmie"):
        super().__init__(age)
        self.matiere_enseignee=matiere
        
    def enseigner(self):
        print("Le cours va commencer.")
        

        

professeur=Professeur(40)

eleve=Eleve()

eleve.bonjour()
eleve.aller_en_cours()
eleve.modifier_age(15)

professeur.bonjour()
professeur.enseigner()