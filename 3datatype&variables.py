a = 123 #int
b ="agni" #str
c =True #bool
d =None #NoneType
e =249
f= complex(2,8) #complex
print(f)
print(b)
print(a+e) #int
print(a+e+f) #complex
print("type of a is",type(a)) #int
print("type of b is",type(b)) #str
print("type of c is",type(c)) #bool
print("type of d is",type(d)) #NoneType
print("type of f is",type(f)) #complex
list1=[a,b,c,d,["Agni","football"]]
print(list1) #[123, 'agni', True, None, ['Agni', 'football']]
tuple1=(("Agni","football"),a,b,c,d)  #immutable
print(tuple1) #(('Agni', 'football'), 123, 'agni', True, None)
dict1={"name":"Agni","roll number":"16900323022"} #mapped data
print(dict1) #{'name': 'Agni', 'roll number': '16900323022'}
print(type(list1)) #list
print(type(tuple1)) #tuple
print(type(dict1)) #dict