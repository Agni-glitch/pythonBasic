class Employee:
    def __init__(self,name ,id):
        self.name=name
        self.id=id
    def showDetails(self):
        print(f"The name of Employee id {self.id} is {self.name}")
class Programmer(Employee):
    def __init__(self,name,id,lang):
        self.lang=lang
        super().__init__(name,id)
    def showlang(self):
        print(f"He uses {self.lang} for coding")
        super().showDetails()
e1=Programmer("Agni",15000,"java")
e1.showlang()