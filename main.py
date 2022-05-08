import requests
from bs4 import BeautifulSoup

URL = "https://www.hollywoodreporter.com/lists/100-best-films-ever-hollywood-favorites-818512"

response = requests.get(URL)
website_html = response.text

soup = BeautifulSoup(website_html, "html.parser")
print(soup.prettify())

all_movies = soup.find_all(name="h2", class_="title")
all_indexes = soup.find_all(selector=".list-item__index")

movie_titles = [movie.getText() for movie in all_movies]
# reverse the list to have the first on top
movies = movie_titles[::-1]

with open("movies.txt", mode="w") as file:
    index = 1
    for movie in movies:
        file.write(f"{str(index)}) {movie}\n")
        index += 1
