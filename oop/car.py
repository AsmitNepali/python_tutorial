# Class for define types of variable in python 
# 1. Class variable
    # The class varable is define on above the  constructor
# 2. Instance variable
    # Instance variable is create on __init__ function or constructor
class Car():
    wheel = 4 # This wheel vriable is class variable
    def __init__(self):
        # self.company and self.mil is a instance variable
        self.company = "Hundai"
        self.mil = "55"

c1 = Car()
c1.company = "BMW" 


print(c1.company)
print(Car.wheel)