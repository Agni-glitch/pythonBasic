marks=[3,5,10]
print(marks) #[3, 5, 10]
print(len(marks)) #3
print(marks[2]) #10
# print(marks[4]) #error
marks1=[3,54,True,"agni"]
print(marks1[-2]) #True
if "agni" in marks1:
    print("Yes") #Yes
else:
    print("No")

# for string
if "Ro" in "Agni Roybar":
    print("Yes") #Yes

print(marks1[0:4:2]) #[3, True]

lst=[i*i for i in range(4)]
print(lst) #[0, 1, 4, 9]

lst=[i*i for i in range(10) if i%2==0]
print(lst) #[0, 4, 16, 36, 64]