class Shape:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def area(self):
        return self.x*self.y
class circle(Shape):
    def __init__(self,r):
        self.r=r
        super().__init__(r,r)
    def area(self):
        # return 3.14*self.r*self.r
        return 3.14*super().area()

rectrangle=Shape(3,6)
print(rectrangle.area())
c1=circle(5)
print(c1.area())