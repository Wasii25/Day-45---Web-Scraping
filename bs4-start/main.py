from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/")
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")

articles = soup.find_all(name="span", class_="titleline")
article_texts = []
article_links = []

for article_tag in articles:
    article_text = article_tag.getText()
    article_texts.append(article_text)
    article_link = article_tag.get("href")
    article_links.append(article_link)

article_upvote_tags = soup.find_all("span", class_="score")
articles_upvote = [int(upvote.getText().split()[0]) for upvote in article_upvote_tags]

print(articles_upvote.index(max(articles_upvote)))

print(article_texts)
print(article_links)
print(articles_upvote)

