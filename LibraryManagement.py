class Library:
    def __init__(self,book,num):
        self.book=book
        self.num=num
bk=[]
no_of_books=int(input("No of books with there stock: "))
for i in range(no_of_books):
    a=input("Book Name: ")    
    b=int(input("no of books in stock: "))
    book=Library(a,b)
    bk.append(book)
e=''
while(e!='no'):
    e=input("Do you want to take book (yes or no): ").lower()
    if(e=='no'):
        break
    print("stocks available: ")
    for i in bk:
        print(i.book,i.num)
    a=input("What book you want? ")
    b=int(input("Quantity you want: "))
    for i in bk:
        if(i.book==a):
            if(i.num==0 or i.num-b<=0):
                print("sorry stock is not available")
            else:
                i.num-=b