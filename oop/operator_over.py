class Student:
    def __init__(self,m1,m2):
        self.m1 = m1
        self.m2 = m2
    
    def __add__(self,other):
        m1 = self.m1 + other.m1
        m2 = self.m2 + other.m2
        s3 = Student(m1,m2)
        return s3
    
    def __gt__(self,other):
        s1 = self.m1 + other.m2
        s2 = self.m1 + other.m2
        if s1>s2:
            return True
        else:
            return False 

    def __mul__(self,other):
       pro1 = self.m1 * self.m2
       pro2 = self.m2 * self.m2

        t_pro = Student(pro1,pro2)
        return t_pro


s1 = Student(2,3)
s2 = Student(4,6)

s3 = s2+s1

if s1 > s2:
    print("s1 is greater than s2")
else:
    print("s2 is greater than s1")

print(s3.m1)

s4 = s1*s2

print(s4.pro1)

