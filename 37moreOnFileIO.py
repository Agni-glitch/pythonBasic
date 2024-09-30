# f = open("myfile.txt",'r')
# while True:
#     line=f.readline()
#     if not line:
#         break
#     print(line)
f=open('marks.txt','w')
lines=['34,42,45\n','39,46,32\n','26,49,41']
f.writelines(lines)
f.close

f=open('marks.txt','r')
while True:
    line=f.readline()
    if not line:
        break
    marks= line.split(',')
    # print(marks)
    print(f"maths:{marks[0]}")
    print(f"physics:{marks[1]}")
    print(f"chemistry:{marks[2]}")
    # print(line)