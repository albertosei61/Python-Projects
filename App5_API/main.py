import requests

api_key = "9d558d805e6543d6b51f1ac0b7d509a2"
url = "https://newsapi.org/v2/everything?q=tesla&from=2024-02-29&sortBy=" \
    "publishedAt&apiKey=9d558d805e6543d6b51f1ac0b7d509a2"
#Making request
request = requests.get(url)

#Using json to get dictionary or you can use text to get a str
content = request.json()
for article in content["articles"]:
    print(article["title"])
    print(article["description"])