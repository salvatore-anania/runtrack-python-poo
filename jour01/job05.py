class Animal:
    def __init__(self):
        self.age=0
        self.prenom=""
    
    def get_age(self):
        return self.age
    
    def get_prenom(self):
        return self.prenom
    
    def viellir(self):
        self.age+=1
        return self.age
    
    def nommer(self,prenom):
        self.prenom=prenom
        
    
chat=Animal()


print(f"L'animal a {chat.get_age()} ans.")
chat.viellir()
print(f"L'animal a {chat.get_age()} ans.")
chat.nommer("chabrian")
print(f"L'animal s'appelle {chat.get_prenom()}.")

