import requests
from pyquery import PyQuery as pq

# r = requests.get('https://jsonplaceholder.typicode.com/todos/1', auth=('user', 'pass'))
# print(r.headers['content-type']) #application/json; charset=utf-8
# print(r.status_code)
# print(r.encoding) #utf-8
# print(r.json()) #python dict

#using pyquery module

r = requests.get('https://www.codewithharry.com/', auth=('user', 'pass'))
# print(r.headers['content-type']) #text/html; charset=utf-8
# print(r.content)
# print(r.text)
# doc=pq(r.content)
# print(doc("ul li").text())
# print(doc("div.bg-purple-100").text()) #for class
# print(doc("div#__next").text()) #for id

#using bs4 module

from bs4 import BeautifulSoup
soup=BeautifulSoup(r.text,'html.parser')
print(soup.prettify())
# for i in soup.find_all('h2'):
#     print(i)
#     print(i.text)

#post request

# url='https://jsonplaceholder.typicode.com/posts'
# data={
#     "id": 1,
#     "title": 'foo',
#     "body": 'bar',
#     "userId": 1,
# }
# headers= {
#     'Content-type': 'application/json; charset=UTF-8',
# }
# res=requests.post(url,headers=headers,json=data)
# print(res.text)