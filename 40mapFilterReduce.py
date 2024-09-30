def cube(x):
    return x*x*x
print(cube(3))
l=[1,2,3,4,5,6]
newl=list(map(cube,l)) #[1, 8, 27, 64, 125, 216]
print(newl)

newnewl = list(filter(lambda x:x>50,newl)) #[64, 125, 216]
print(newnewl)

from functools import reduce as r
sum= r(lambda x,y:x+y,l)
print(sum) #21
