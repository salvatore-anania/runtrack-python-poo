class Voiture:
    def __init__(self):
        self.__marque="generique"
        self.__modele="generique"
        self.__annee=2020
        self.__kilométrage=50000
        self.__en_marche=False
        self.__reservoir=50
    
    def get_marque(self):
        return self.__marque
    
    def get_modele(self):
        return self.__modele
    
    def get_annee(self):
        return self.__annee
    
    def get_kilometrage(self):
        return self.__kilométrage
    
    def get_enMarche(self):
        if self.__en_marche:
            return "en marche"
        else:
            return "à l'arrêt"
        
    def get_reservoir(self):
        return self.__reservoir
    
    def set_marque(self,marque):
        self.__marque=marque
    
    def set_modele(self,modele):
        self.__modele=modele
    
    def set_annee(self,annee):
        self.__annee=annee
    
    def set_kilometrage(self,kilométrage):
        self.__kilométrage=kilométrage
    
    def change_enMarche(self):
        self.__en_marche=not self.__en_marche
    
    def set_reservoir(self,litre):
        self.__reservoir=litre
        
    def demarrer(self):
        if self.get_enMarche()=="à l'arrêt" and self.verifier_plein()>5:
            self.change_enMarche()
        elif self.verifier_plein()<5:
            print("Impossible de démarrer plus d'essence")
        else:
            print("Impossible de démarrer")
        
    def arreter(self):
        if self.get_enMarche()=="en marche":
            self.change_enMarche()
        else:
            print("Voiture déjà à l'arrêt")
        
    def verifier_plein(self):
        return self.__reservoir
    
    def info(self):
        print(f"Voiture de marque {self.get_marque()}, modele {self.get_modele()}, datant de {self.get_annee()} avec {self.get_kilometrage()} kilometres,qui est {self.get_enMarche()} et le reservoir est à {self.get_reservoir()}")
    
voiture=Voiture()
voiture.info()
voiture.demarrer()
voiture.info()
voiture.arreter()
voiture.arreter()
voiture.info()
voiture.set_reservoir(4)
voiture.demarrer()