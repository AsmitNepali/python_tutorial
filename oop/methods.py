class Student():
    school = "BrahmaRupa"
    def __init__(self,m1,m2,m3,m4):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3
        self.m4 = m4
    #instance Method
    def avg(self):
        return(self.m1+self.m2+self.m3+self.m4)/3

    #class method
    @classmethod
    def info(cls):
        return cls.school

    #static method
    @staticmethod
    def subject():
        print("This is subject method")


    
s1 = Student(12,34,45,56)
print(s1.avg())
print(Student.info())
Student.subject()