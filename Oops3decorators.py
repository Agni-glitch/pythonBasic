def greet(fx):
    def mfx(*args,**kwargs):
        print("Good morning")
        fx(*args,**kwargs)
        print("Thanks")
    return mfx
@greet
def hello():
    print("Hello, World")
hello()
# greet(hello)()

def add(a,b):
    print(a+b)
greet(add)(4,6)

# Good morning
# Hello, World
# Thanks
# Good morning
# 10
# Thanks