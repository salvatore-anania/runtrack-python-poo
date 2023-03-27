class Operation:
    def __init__(self):
        self.number1=1
        self.number2=2
    
    def get_number1(self):
        return self.number1
    
    def get_number2(self):
        return self.number2
    
test=Operation()

print(f"Le nombre 1 est {test.get_number1()}")
print(f"Le nombre 2 est {test.get_number2()}")
        