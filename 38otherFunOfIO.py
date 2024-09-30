# with open('file.txt','r') as f:
#     f.seek(5)
#     data=f.read(5) #not a
#     print(f.tell()) #10
#     print(data)

with open('samplefile.txt','w') as f:
    f.write('Hello, World!')
    f.truncate(5)
with open('samplefile.txt','r') as f:
    print(f.read()) #Hello