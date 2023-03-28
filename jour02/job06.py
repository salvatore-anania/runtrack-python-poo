class Vehicule:
    def __init__(self,marque="generique",modele="generique",annee=2020,prix=10000):
        self.__marque=marque
        self.__annee=annee
        self.__prix=prix
        self.__modele=modele

    def get_marque(self):
        return self.__marque
    
    def get_annee(self):
        return self.__annee
        
    def get_prix(self):
        return self.__prix
        
    def get_modele(self):
        return self.__modele
    
    def set_marque(self,marque):
        self.__marque=marque
    
    def set_modele(self,modele):
        self.__modele=modele
    
    def set_annee(self,annee):
        self.__annee=annee
        
    def set_prix(self,prix):
        self.__prix=prix
        
    def demarrer(self):
        print("Attention, je roule !")

    def informationsVehicule(self):
        print(f"Voiture de marque {self.get_marque()}, modele {self.get_modele()}, datant de {self.get_annee()} coutant {self.get_prix()} Euros.")
    




class Voiture(Vehicule):
    def __init__(self,marque,modele,annee,prix):
        super().__init__(marque,modele,annee,prix)
        self.__portes=4
    
    def get_portes(self):
        return self.__portes 
    
    def set_portes(self,portes):
        self.__portes=portes
        
    def demarrer(self):
        print("La voiture a démarré, attention aux pieds !")
    
    def informationsVehicule(self):
        super().informationsVehicule()
        print(f"La voiture a {self.get_portes()} portes.")
        
class Moto(Vehicule):
    def __init__(self,marque,modele,annee,prix):
        super().__init__(marque,modele,annee,prix)
        self.__roues=2
    
    def get_roues (self):
        return self.__roues 
    
    def set_roues(self,roues):
        self.__roues=roues
        
    def demarrer(self):
        print("La moto a démarré, attention à la vitesse !")
    
    def informationsVehicule(self):
        super().informationsVehicule()
        print(f"La moto a {self.get_roues()} roues.")
    
    
voiture=Voiture("Mercedes","classe A",2020,18500)
voiture.informationsVehicule()
voiture.demarrer()

moto=Moto("Yamaha","1200 Vmax",1987,4500)
moto.informationsVehicule()
moto.demarrer()
