import multiprocessing
from concurrent.futures import ProcessPoolExecutor
import requests
import os

def DownloadFile(url,i):
    # name = url.split('/')[-1]
    print(f"started downloading {i}")
    os.makedirs('files', exist_ok=True)
    r = requests.get(url,allow_redirects=True)
    file_path=f'files/{i}file.jpg'
    # f=open(f'files/{i}file.jpg', 'wb').write(r.content)
    with open(file_path, 'wb') as f:
        f.write(r.content)
    print(f"finished downloading {i}")
    return i
if __name__ == '__main__':
    url="https://t4.ftcdn.net/jpg/03/10/90/90/360_F_317254576_lKDALRrvGoBr7gQSa1k4kJBx7O2D15dc.jpg"

    # pros=[]
    # for i in range(5):
    #     # print(DownloadFile(url,i))
    #     p= multiprocessing.Process(target=DownloadFile,args=[url,i])
    #     p.start()
    #     pros.append(p)
    # for p in pros:
    #     p.join()

    with ProcessPoolExecutor() as ex:
        urls=[url for i in range(5)]
        # urls=[url]*5
        l=[i for i in range(5)]
        results=ex.map(DownloadFile,urls,l)
        for r in results:
            print(r)