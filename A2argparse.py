# example of command line utility---> curl
#curl https://cdn.britannica.com/41/156441-050-A4424AEC/Grizzly-bear-Jasper-National-Park-Canada-Alberta.jpg --output bear.jpg

import argparse
import requests

def download_file(url,local_filename):
    if local_filename is None:
        local_filename = url.split('/')[-1]
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        with open(local_filename, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192):
                f.write(chunk)
    return local_filename
parser = argparse.ArgumentParser()
parser.add_argument('url',help='url of file to download')
# parser.add_argument('output',help='name you want to save')
parser.add_argument('-o','--output',help='name you want to save',default=None)
args=parser.parse_args()
print(args.url)
print(args.output)
download_file(args.url,args.output)

#python -u "c:\Users\AGNI\programming\python\pythonBasic\A2argparse.py" https://cdn.britannica.com/41/156441-050-A4424AEC/Grizzly-bear-Jasper-National-Park-Canada-Alberta.jpg bear.jpg

#python -u "c:\Users\AGNI\programming\python\pythonBasic\A2argparse.py" https://cdn.britannica.com/41/156441-050-A4424AEC/Grizzly-bear-Jasper-National-Park-Canada-Alberta.jpg -o bear.jpg 