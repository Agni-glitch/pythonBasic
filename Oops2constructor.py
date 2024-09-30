class Person:
    def __init__(self,n,o):
        self.name=n
        self.occ=o #returns None
    def info(self):
        print(f"{self.name} is a {self.occ}")
a=Person("Agni","Software Engineer")
b=Person("Akash","Java Developer")
a.info()
b.info()