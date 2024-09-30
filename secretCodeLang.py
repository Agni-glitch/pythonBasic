import random
import string
def randomChar():
    a=""
    for i in range(3):
        r=random.choice(string.ascii_lowercase)
        a+=r
    return a
st=input("Enter a string to be coded: ")
l1=st.split(" ")
s2=[]
coding=False
if(coding):
    for i in l1:
        if(len(i)>=3):
            r1=randomChar()
            r2=randomChar()
            s2.append(r1+i[1:]+i[0]+r2)
        else:
            s2.append(i[::-1])      
    st2=""
    for i in s2:
        st2+=(i+" ")
    print(st2)
else:
    for i in l1:
        if(len(i)>=3):
            s2.append(i[-4:-3]+i[3:-4])
        else:
            s2.append(i[::-1])  
    st2=""
    for i in s2:
        st2+=(i+" ")
    print(st2)