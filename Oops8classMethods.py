# class Employee:
#     company="Apple"
#     def show(self):
#         print(f"The name in {self.name} and the company is {self.company}")
#     @classmethod
#     def changeCompany(cls,newCompany):
#         cls.company=newCompany
# e1=Employee()
# e1.name="Agni"
# e1.show()
# e1.changeCompany("Microsoft")
# e1.show()
# print(e1.company)
# e2=Employee()
# print(e2.company) #changed

#class methods as alternative constructors

class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    @classmethod
    def fromStr(cls,string):
        return cls(string.split("-")[0],int(string.split("-")[1]))
e1=Employee("Agni",15000)
print(e1.name,e1.salary)

string="Agni-13000"
e2=Employee.fromStr(string)
print(e2.name,e2.salary)