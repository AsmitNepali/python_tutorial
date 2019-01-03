import sys
sys.setrecursionlimit(200)
i = 0 
def Myname():
    global i
    i +=1
    print("Your name is Asmit Nepali",i)
    Myname()

Myname()

print(sys.getrecursionlimit())