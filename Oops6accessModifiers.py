class Employee:
    def __init__(self):
        # self.name="Agni" #default public
        self.__name="Agni" #private
        # self._name="Protected"
a=Employee()
# print(a.__name) #error
print(a._Employee__name) #name mangiling
print(a.__dir__()) #all methods