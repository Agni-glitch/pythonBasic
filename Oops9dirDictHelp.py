class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
e1=Employee("Agni",45000)
l1=[2,3,4,5,6]
print(dir(l1))
print(l1.__add__)#dunder methods
# print(e1.__dir__())
# print(dir(e1))
# print(e1.__dict__)
# print(help(e1))