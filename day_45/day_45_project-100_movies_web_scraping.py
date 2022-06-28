from bs4 import BeautifulSoup
import requests

response = requests.get(
    "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")

empire_html = response.text

soup = BeautifulSoup(empire_html, "html.parser")

movie_list = soup.find_all(name="h3", class_="title")
movie_names = [movie.getText() for movie in movie_list][::-1]

with open("./day_45/100_movie_list.txt", mode="w", encoding="utf-8") as f:
    for _ in movie_names:
        f.write(f"{_}\n")

# print(movie_names)
