from typing import Any


class Employee:
    def __init__(self,name):
        self.name =name
    def __len__(self):
        i=0
        for c in self.name:
            i+=1
        return i
    # def __str__(self):
    #     return f"The name of the employee is {self.name}"
    def __repr__(self):
        return f"The name of the employee is {self.name}"
    def __call__(self):
        print(f"I am {self.name}")
e=Employee("Agni")
print(e.name) #Agni
print(len(e)) #4
print(e)     #The name of the employee is Agni
e() #I am Agni