x= 4
print(x) #4
def hello():
    global x
    x=5
print(x) #4
hello() 
print(x) #5