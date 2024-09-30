class Person:
    name="Agni" #class variable
    occupation="Student"
    netWorth=100
    def info(self):
        print(f"{self.name} {self.occupation} {self.netWorth}")
a=Person()
a.name="Akash" #instance var
a.occupation="college student"
print(a.name,a.occupation)
a.info()