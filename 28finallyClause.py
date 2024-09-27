def fun():
    try:
        l=[3,4,5,8,2]
        ip=int(input("enter a index: "))
        print(l[ip])
        return 1
    except IndexError:
        print("index error")
        return 0
    finally:
        print("I am always executed")
x=fun()
print(x)
# enter a index: 7
# index error
# I am always executed
# 0