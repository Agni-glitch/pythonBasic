def factorial(n):
    if(n==0 or n==1):
        return n
    else:
        return n*factorial(n-1)
print(factorial(5))
#120
def fibonacci(n):
    if(n==0 or n==1):
        return n
    else:
        return fibonacci(n-1)+fibonacci(n-2)
print(fibonacci(6))
#8