from threading import *
from time import sleep

class Fname(Thread):
    def run(self):  
        for i in range(500):
            print("Asmit")
            sleep(1)

class Lname(Thread):
    def run(self):
        for i in range(500):
            print("Nepali")
            sleep(1)

f1 = Fname()
l1 = Lname()

f1.start()
sleep(0.2)
l1.start()

f1.join()
l1.join()

print("Have a good day")