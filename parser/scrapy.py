from bs4 import BeautifulSoup
import requests

URL = "https://w139.zona.plus/"

HEADERS = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "User-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36"

}


def get_requests(url, params=''):
    req = requests.get(url, headers=HEADERS, params=params)
    return req


def get_data(html):
    soup = BeautifulSoup(html, "html.parser")
    items = soup.find_all("li", class_="item")
    movies = []
    for item in items:
        movies.append(
            {
                "link": URL + item.find("a", class_="link").get("href"),
                "title": item.find("h3", class_="title").get_text(),
                # "image": URL + item.find("div", class_="cover-wrap").find("div").get("style")
            }
        )

    return movies


def scrapy_script():
    html = get_requests(URL)
    if html.status_code == 200:
        movies = []
        for page in range(1, 3):
            html = get_requests(f"https://w139.zona.plus/")
            movies.extend(get_data(html.text))
        return movies[0].values()
    else:
        raise Exception("Error in scrapy script function")


html = get_requests(URL)
get_data(html.text)
