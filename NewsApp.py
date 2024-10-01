import requests
r = requests.get('https://newsapi.org/v2/everything?q=tesla&from=2024-09-01&sortBy=publishedAt&apiKey=0175f2ba50344b36b523c7b00ccf4101')
for i in range(100):
    print(f"{i+1}.  {r.json()['articles'][i]['content']}\n")