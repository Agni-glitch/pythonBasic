from functools import lru_cache
import time
@lru_cache(maxsize=None)
def fx(n):
    time.sleep(2)
    return n*5
#slow
print(fx(3))
print("done for 3")
print(fx(10))
print("done for 10")
print(fx(40))
print("done for 40")
#fast
print(fx(3))
print("done for 3")
print(fx(10))
print("done for 10")
print(fx(40))
print("done for 40")
print(fx(3))
print("done for 3")
print(fx(10))
print("done for 10")
print(fx(40))
print("done for 40")
#slow
print(fx(60))
print("done for 60")