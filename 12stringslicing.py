fruit ="mango"
notyourtype = len(fruit)
print(notyourtype)
print(fruit[0:5]) #last character is eleminated
#slicing
print(fruit[:5]) #same as 0:5
print(fruit[:]) #same as 0:5
print(fruit[1:]) #same as 1:5
print(fruit[1:-3]) #1:2
print(fruit[1:len(fruit)-3]) #1:2
print(fruit[-1:-2]) #space as output
print(fruit[-4:3]) #1:3{len(fruit)-1:3}
#looping
for i in fruit:
    print(i)
