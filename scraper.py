import requests
from bs4 import BeautifulSoup


def scrape_google_news(query):
    url = f"https://news.google.com/search?q={query}"
    res = requests.get(url)
    soup = BeautifulSoup(res.text, "html.parser")

    articles = []
    for item in soup.select("article"):
        text = item.get_text()
        if text:
            articles.append(text)

    return articles


def scrape_reddit(query):
    url = f"https://www.reddit.com/search.json?q={query}"
    headers = {"User-Agent": "Mozilla/5.0"}

    try:
        res = requests.get(url, headers=headers).json()
        posts = []
        for post in res["data"]["children"]:
            posts.append(post["data"]["title"])
        return posts
    except:
        return []
