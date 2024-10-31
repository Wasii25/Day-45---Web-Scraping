import requests
from bs4 import BeautifulSoup

URL = "https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇

response = requests.get(URL)
soup = BeautifulSoup(response.text, "html.parser")

articles = soup.find_all(name="h3", class_="listicleItem_listicle-item__title__BfenH")
print(articles)

with open("movies.txt", "w") as file:
    for article in articles[::-1]:
        file.write(f"{article.text}\n")