class Pycharm:
    def execute(self):
        print("Compling")
        print("Running")

class MyEditor:
    def execute(self):
        print("Spell Check")
        print("Convention Check")
        print("Compling")
        print("Running")

class Laptop:
    def code(self,ide):
        ide.execute()

ide = MyEditor()
lap1 = Laptop()
lap1.code(ide)
        
