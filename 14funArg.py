#function Arguments

def average1(a,b=0): #default argument b=0, we should provide the valuer of a positively
    print("average of 2 numbers= ",(a+b)/2)

average1(34) #a=34,b=0 #average of 2 numbers=  17.0
average1(45,67) #a=45,b=67 #average of 2 numbers=  56.0

def name1(fname,mname="Agni",lname="Roybar"):
    print("hello",fname,mname,lname)

name1('Mrs') #hello Mrs Agni Roybar
name1("Mrs","john","smith") #hello Mrs john smith

def average2(*numbers):
    print(type(numbers)) #<class 'tuple'>
    sum=0
    for i in numbers:
        sum = sum+i
    print("the average of the numbers= ")
    return sum/len(numbers)

c = average2(1,2,3,4,5,6,7,8,9,10)
print(c)

def name2(**name):
    print(type(name)) #<class 'dict'>
    print("hello",name["fname"],name["mname"],name["lname"])

name2(fname="Mrs",mname="Agni",lname="Roybar")