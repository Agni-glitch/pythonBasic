import threading
import time 
from concurrent.futures import ThreadPoolExecutor
def func(seconds):
    time.sleep(seconds)
    print(f"Sleeping for {seconds} seconds")
    return seconds

# def main():
#     time1=time.perf_counter()
#     # func(4)
#     # func(2)
#     # func(1)
#     # time2=time.perf_counter()
#     # print(time2-time1)

#     t1=threading.Thread(target=func,args=[3])
#     t2=threading.Thread(target=func,args=[4])
#     t3=threading.Thread(target=func,args=[6])
#     t1.start()
#     t2.start()
#     t3.start()
#     t1.join()
#     t2.join()
#     t3.join()
#     time2=time.perf_counter()
#     print(time2-time1)

def pooling():
    with ThreadPoolExecutor() as executor:
        # future2 = executor.submit(func,4)
        # future1 = executor.submit(func,3)
        # future3 = executor.submit(func,5)
        # print(future1.result())
        # print(future2.result())
        # print(future3.result())
        l=[4,3,5]
        results=executor.map(func,l)
        for result in results:
            print(result)
pooling()