x1= "23"
x2= "45"
print(x1+x2) #2345

#implicit
a ="28"
b = 7
c = int(a) + b
print(c)
# a="harry" cannot be typecast ot int() besause it is a string
#explicit
e =249
f= complex(2,8)
g= e+f
print(g)
print(type(e))
print(type(f))
print(type(g)) #always follows higher data

"""
2345
35
(251+8j)
<class 'int'>
<class 'complex'>
<class 'complex'>
"""