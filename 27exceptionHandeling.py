a = input("please give a number: ")
print(f"multiplication table of {a}")
try:
    for i in range(1,10):
        print(f"{int(a)} x {i} = {int(a)*i}")
# except Exception as e:
#     print(e)
#     print("Invalid Input")
except ValueError:
    print("value error")#value error
except IndexError:
    print("Index error")
print("end")
# please give a number: agni
# multiplication table of agni
# invalid literal for int() with base 10: 'agni'
# Invalid Input
# end