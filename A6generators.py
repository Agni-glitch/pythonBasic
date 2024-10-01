#less memory consumption
def myGenerator():
    count=0
    for i in range(10):
        count+=2
        yield count

a=myGenerator()
print(next(a))
print(next(a))
print(next(a))
print(next(a))

# for i in a:
    # print(i)