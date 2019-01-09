class Computer():

    # __init__ function is contructor in python which is called atuomatically when method is calling
    def __init__(self,cpu,gen):
        self.cpu = cpu
        self.gen = gen    

    def config(self): 
        print("Hello Alien, My computer has",self.cpu,self.gen)

    def compare(self,others):
        if self.gen == others.gen:
            print("They are same")
        else:
            print("They are not same")

com1 = Computer('i5','7th')
com2 = Computer('i7', '8th')
# Here we just pass only one arguments on compare function but above in class the method compage have two formal parameters
# they are self and others, in this case the first parameters com1 became self
com1.compare(com2)

# Here com1 is a object of class Computer and functions are method

Computer.config(com1)
Computer.config(com2)