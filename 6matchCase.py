x = int(input("enter a number:"))
match x:
    case 18:
        print("you can drive")
    case _ if x>18:
        print("you can easily drive")
    case _ if x<18 :
        print("you can not drive")
# no break statement is used here