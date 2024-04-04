import requests
from message_email import email_conn

topic = "tesla"
api_key = "9d558d805e6543d6b51f1ac0b7d509a2"
url = "https://newsapi.org/v2/everything?" \
    f"q={topic}&" \
        "from=2024-03-04&" \
            "sortBy=publishedAt&" \
                "apiKey=9d558d805e6543d6b51f1ac0b7d509a2&" \
                    "language=en"
#Making request
request = requests.get(url)

#Using json to get dictionary or you can use text to get a str
content = request.json()
email_message = ""
for article in content["articles"][0:20]:
    title = article['title'].encode('utf-8', 'ignore').decode('utf-8')
    description = article['description']
    if description is not None:
        description = description.encode('utf-8', 'ignore').decode('utf-8')
    else:
        description = "No description available"
    email_message += f"Subject: Today's news\nTitle: {title}\nDescription: {description}\nUrl: {url}\n"

email_conn(email_message)