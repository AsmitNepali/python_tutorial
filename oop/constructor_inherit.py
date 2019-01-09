class A():
    def __init__(self):
        print("This is from init A")

    def feature1(self):
        print("Feature 1 working")
    
    def feature2(self):
        print("Feature 2 working")


class B(A):
    def __init__(self):
        super().__init__()
        print("This is from init B")

    def feature3(self):
        print("Feature 3 working")
    
    def feature4(self):
        print("Feature 4 working")

class C(A,B):
    def __init__(self):
        super().__init__()
        print("This is from init C")

    def feature5(self):
        print("Feature 5 working")
    
    def feature6(self):
        print("Feature 6 working")

a1 = B()