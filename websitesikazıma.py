import requests
from bs4 import BeautifulSoup

header = {"user-agent": "Mozilla/5.0"}
url = "https://www.milliyet.com.tr/"
get = requests.get(url, headers=header)
content = get.content
soup = BeautifulSoup(content,"html.parser")
titles = soup.find_all("div",{"class": "main-card__bg"})

for i in titles:
    print(i)
