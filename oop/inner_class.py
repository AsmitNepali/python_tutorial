class Student():

    def __init__(self,name,roll):
        self.name = name
        self.roll = roll
        self.lap = self.Laptod()
    
    def show(self):
        print(self.name,self.roll)
    
    class Laptod:
        def __init__(self):
            self.brand = "DELL"
            self.cpu = "i5"
            self.ram = "4"

        def show(self):
            print(self.brand,self.cpu,self.ram)


    

s1 = Student("Asmit",4)
s2 = Student("Joe",5)
lap1 = Student.Laptod()

lap1.show()

s1.show()
