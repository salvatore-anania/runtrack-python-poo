class Student:
    def __init__(self,nom,prenom,numero):
        self.__nom=nom
        self.__prenom=prenom
        self.__ID=numero
        self.__credits=0
        self.__level=self.__studentEval()
    
    def get_nom(self):
        return self.__nom
    
    def get_prenom(self):
        return self.__prenom
    
    def get_ID(self):
        return self.__ID
    
    def get_credits(self):
        return self.__credits
    
    def get_level(self):
        return self.__level
    
    def set_level(self):
        self.__level=self.__studentEval()
    
    def sePresenter(self):
        return self.__prenom+" "+self.__nom
    
    def add_credits(self,credits):
        if credits>0:
            self.__credits+=credits
        else:
            print("Nombres de credits non valide entrez un nombre superieur à 0")
            
    def __studentEval(self):
        if self.get_credits()>=90:
            return "Excellent"
        elif self.get_credits()>=80:
            return "Très bien"
        elif self.get_credits()>=70:
            return "Bien"
        elif self.get_credits()>=60:
            return "Passable"
        else:
            return "Insuffisant"
        
    def studentInfo(self):
        self.set_level()
        print(f"Nom = {john.get_nom()}")
        print(f"prenom = {john.get_prenom()}")
        print(f"ID = {john.get_ID()}")
        print(f"Niveau = {john.get_level()}")

john=Student("Doe", "John",145)
print(f"l'étudiant s'appelle {john.sePresenter()} porte le numero {john.get_ID()} et à {john.get_credits()} crédits")
john.add_credits(-34)
john.add_credits(10)
john.add_credits(10)
john.add_credits(60)
print(f"l'étudiant s'appelle {john.sePresenter()} porte le numero {john.get_ID()} et à {john.get_credits()} crédits")
john.studentInfo()