m=(1)
print(type(m)) #<class 'int'>
m=(1,)
print(type(m)) #<class 'tuple'>

tup=(34,78,90,True,"Agni") #immutable
print(tup) #(34, 78, 90, True, 'Agni')
print(tup[2]) #90

m=list(tup)
print(m) #[34, 78, 90, True, 'Agni']

if 90 in tup:
    print("yes")
    
print(tup[0:5:2]) #(34, 90, 'Agni')