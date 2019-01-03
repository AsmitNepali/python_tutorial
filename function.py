# Here in function some points are important they are
# Position
# Keyword
# default
# variable length
def sum(a,*b): # *b means b have multiple value
    c = a
    for i in b:
        c += i
    print(c)
sum(5,7,6,3,4)

def person(name, **data): # **data for accept argument with keyword
    print(name)
    for  i,j in data.items():
        print(i,j)
        
person('Asmit', age=19, address="Pokhara")