class Voiture:
    def __init__(self):
        self.__marque
        self.__modele
        self.__annee
        self.__kilométrage 
        self.__en_marche=False
    
    def get_marque(self):
        return self.__marque
    
    def get_modele(self):
        return self.__modele
    
    def get_annee(self):
        return self.__annee
    
    def get_kilometrage(self):
        return self.__kilométrage
    
    def get_enMarche(self):
        return self.__en_marche
    
    def set_marque(self,marque):
        self.__marque=marque
    
    def set_modele(self,modele):
        self.__modele=modele
    
    def set_annee(self,annee):
        self.__annee=annee
    
    def set_kilometrage(self,kilométrage):
        self.__kilométrage=kilométrage
    
    def set_enMarche(self):
        self.__en_marche=not self.__en_marche