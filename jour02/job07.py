from random import randint
import pygame

class Carte:
    def __init__(self,couleur,valeur):
        self.__couleur=couleur
        self.__valeur=valeur
        
    def get_valeur(self):
        return self.__valeur
    
    def affiche(self):
        print( f"{self.__valeur} de {self.__couleur}")
    
class Jeu:
    def __init__(self):
        self.__paquet=[]
        
    def remplir_paquet(self):
        couleur=["coeur","carreau","trefle","pique"]
        change_color=0
        for i in range(1,53):
            if i%13==1:
                self.__paquet.append(Carte(couleur[change_color],11))
            elif i%13==0:
                self.__paquet.append(Carte(couleur[change_color],10))
                change_color+=1
            elif i%13==11:
                self.__paquet.append(Carte(couleur[change_color],10))
            elif i%13==12:
                self.__paquet.append(Carte(couleur[change_color],10))
            else:
                self.__paquet.append(Carte(couleur[change_color],i%13))
        return self.__paquet
    
    def get_paquet(self):
        return self.__paquet
    
    def __set_paquet(self,paquet):
        self.__paquet=paquet
    
    def distribuer(self):
        pioche =randint(0,len(self.__paquet)-1)
        piocher=self.__paquet[pioche]
        self.__paquet.remove(piocher)
        return piocher

class Main():
    def __init__(self):
        self.__main=[]
        
    def get_paquet(self):
        return self.__main
    
    def piocher(self,carte):
        self.__main.append(carte)
        
    def affiche(self):
        for carte in self.__main:
            carte.affiche()
            
    def calcul_main(self):
        total_main=0
        for carte in self.__main:
            total_main+=carte.get_valeur()
            
        return total_main
    
    def main_plus_forte(self,main):
        if self.calcul_main()<main.calcul_main() and main.calcul_main()<=21:
            print("Vous avez perdu")
        else:
            print("Vous avez gagne")

paquet=Jeu()
joueur=Main()
croupier=Main()
paquet.remplir_paquet()
piocher=True
perdu=False
for i in range (2):
    joueur.piocher(paquet.distribuer())
    croupier.piocher(paquet.distribuer())
while piocher:
    print("Votre main :")
    joueur.affiche()
    print("tirer une carte : oui(O) non(N)")
    if input()=="O":
        joueur.piocher(paquet.distribuer())
    else:
        piocher=False
if joueur.calcul_main()>21:
    perdu=True
piocher=True

while piocher and not perdu:
    print("\nla main du croupier :")
    croupier.affiche()
    if croupier.calcul_main()<17:
        croupier.piocher(paquet.distribuer())
    else:
        piocher=False

if not perdu:
    joueur.main_plus_forte(croupier)
else:
    print("Vous avez perdu")
