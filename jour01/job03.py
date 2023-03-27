class Operation:
    def __init__(self):
        self.number1=1
        self.number2=2
    
    def get_number1(self):
        return self.number1
    
    def get_number2(self):
        return self.number2
    
    def addition(self):
        print(f"Résultat de l'addition : {self.number1+self.number2}")
    
test=Operation()

test.addition()
        