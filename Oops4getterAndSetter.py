class myClass:
    def __init__(self,value):
        self._value=value
    def show(self):
        print(f"{self._value}")
    @property
    def ten_value(self):
        return 10*self._value
    @ten_value.setter
    def ten_value(self,newVal):
        self._value=newVal/10
    
obj=myClass(10)
print(obj.ten_value)
obj.show()
obj.ten_value=67
print(obj.ten_value)
obj.show()

# obj._value=20
# print(obj._value)