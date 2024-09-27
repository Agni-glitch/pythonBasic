# conditional statement <,>,<=,>=,==,!=
# and/or

print("write the marks you got in your exam:")
a=input("marks obtained in phy: ")
b=input("marks obtained in chem: ")
c=input("marks obtained in math: ")

if((a>b and a>c) and (a != b and a != c)): 
    print(a, " is the largest") 
elif((b>a and b>c) and (b != a and b != c)): 
    print(b, " is the largest") 
elif((c>a and c>b) and (c != a and c != b)): 
    print(c, " is the largest") 
else: 
    print("entered numbers are equal") 

if(a == b and b == c and c == a): 
    print("working") 
else: 
    print("stopped") 


age = 11

if ((age>= 8) and (age<= 12)): 
	print("YOU ARE ALLOWED. WELCOME !") 
else: 
	print("SORRY ! YOU ARE NOT ALLOWED. BYE !") 
