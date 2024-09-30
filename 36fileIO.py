# f = open('myfile.txt','r') # 'r' is default
# text = f.read()
# print(text)
# f = open('myfile.txt','w') #creats new file if not exists
f = open('myfile.txt','a') #append mode
# f = open('myfile.txt','x') #create mode
# f = open('myfile.txt','rb') #read binary
f.write("\nHi itz agni form Bhadreswar")
f.close()

with open("myfile.txt",'a') as f:
    f.write("\nHello world")