class Personne:
    def __init__(self,nom,prenom):
        self.nom=nom
        self.prenom=prenom
    
    def get_nom(self):
        return self.nom
    
    def get_prenom(self):
        return self.prenom
    
    def sePresenter(self):
        return self.prenom+" "+self.nom
    
magicien=Personne("potter","harry")
moi=Personne("anania","salvatore")
acteur=Personne("dujardin","jean")

print(f"Je suis {magicien.sePresenter()}")
print(f"Je suis {moi.sePresenter()}")
print(f"Je suis {acteur.sePresenter()}")
        