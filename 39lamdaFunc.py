double = lambda x:x*2
print(double(5)) #10
cube=lambda x:x*x*x
def funfun(fx,value):
    return fx(value)
print(funfun(cube,3)) #27
a= lambda x,y,z:(x+y+z)/3
print(a(2,4,6)) #4.0