import requests
from send_email import send_mail


topic = "tesla"

api_key = "c1260aba486b4afb8a1a214bfcda77c6"
url = "https://newsapi.org/v2/everything?"\
    f"q='{topic}'&"\
    "from=2022-11-22&sortBy"\
    "=publishedAt&apiKey=c1260aba486b4afb8a1a214bfcda77c6&"\
    "language=eng"

r = requests.get(url)

content = r.json()
email_cont = f"""\
Subject: Today's news

"""
for a in content["articles"][:20]:
    Title = (a["title"])    
    source = (a["url"])
    Author = (a["source"]["Name"])
    news_story = f"""{Title}
{source}
{Author}

"""
    email_cont = email_cont + news_story

email_cont = email_cont.encode("utf-8")

send_mail(email_cont)
print(email_cont)










