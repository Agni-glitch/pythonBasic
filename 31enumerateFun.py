a=[12,45,59,74,43,94]
for index, mark in enumerate(a):
    print(f"{index} has value {mark}")
    print("{}".format(mark)) if mark>=70 else print("low marks")