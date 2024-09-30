class Employee:
    def __init__(self,name ,id):
        self.name=name
        self.id=id
    def showDetails(self):
        print(f"The name of Employee id {self.id} is {self.name}")
class Programmer(Employee):
    def showlang(self,lang):
        print(f"He uses {lang} for coding")
e=Employee("Agni",22)
e.showDetails()
a=Programmer("Agni","T022")
# a.showDetails()
Programmer.showDetails(a) #one default arg is already there 
a.showlang("Python")