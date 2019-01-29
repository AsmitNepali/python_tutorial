# Here in python no way to method overloading

class Student():
    def __init__(self,m1,m2):

        self.m1 = m1
        self.m2 = m2

    def sum(self,a = None, b = None, c = None):
        if a!=None and b!=None and c!=None:
            s = a+b+c
        elif a!=None and b!=None:
            s = a+b
        else:
            s = b

        return s


s1 = Student(45,56)

print(s1.sum(2,3,8))

class A():

    def show(self):
        print("This is show in A")

class B(A):

    def show(self):
        print("This is show in B")

obj1 = B()
obj1.show()