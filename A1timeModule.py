import time

# def usingWhile():
#     i=0
#     while i<1000:
#         print(i)
#         i+=1
# def usingFor():
#     for i in range(1000):
#         print(i)
# init1 = time.time()
# usingWhile()
# t1=time.time()-init1 #0.23541951179504395
# init2 = time.time()
# usingFor()
# t2=time.time()-init2 #0.22669720649719238
# print(t1-t2) #0.032149314880371094

# print(4)
# time.sleep(3)
# print("I am Agni")

t=time.localtime()
print(t)
timestrap = time.strftime("%Y-%m-%d %H:%M:%S")
print(timestrap)