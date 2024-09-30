class Math:
    def __init__(self, num):
        self.num = num
    def addtonum(self,n):
        self.num=self.num+n
    @staticmethod #without using self
    def add(a,b):
        return a+b
a=Math(5)
print(a.num) #5
a.addtonum(6)
print(a.num) #11
print(a.add(a.num,7)) #18