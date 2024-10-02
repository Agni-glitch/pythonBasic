# # import time
import asyncio
import requests
async def func1():
    # await asyncio.sleep(2)
    url = 'http://google.com/favicon.ico'
    r = await asyncio.to_thread(requests.get, url, allow_redirects=True)
    with open('google.ico', 'wb') as f:
        f.write(r.content)
    print('func1')
    return 'I'
async def func2():
    # await asyncio.sleep(2)
    url = 'http://google.com/favicon.ico'
    r = await asyncio.to_thread(requests.get, url, allow_redirects=True)
    with open('google2.ico', 'wb') as f:
        f.write(r.content)
    print('func2')
    return "am"
async def func3():
    # await asyncio.sleep(3)
    url = 'http://google.com/favicon.ico'
    r = await asyncio.to_thread(requests.get, url, allow_redirects=True)
    with open('google3.ico', 'wb') as f:
        f.write(r.content)
    print('func3')
    return 'bad'
async def main():
#one by one
    # task=asyncio.create_task(func1())
    # await func1()
    # await func2()
    # await func3()

#all at a time
    task=await asyncio.gather(
    func1(),
    func2(),
    func3(),)
    print(task)
asyncio.run(main())
