import requests
from bs4 import BeautifulSoup

header = {"user-agent": "Mozilla/5.0"}
url = "https://www.milliyet.com.tr/"
get = requests.get(url, headers=header)
content = get.content
soup = BeautifulSoup(content,"html.parser")
titles = soup.find_all("h3",{"class": "main-card__head"})

for i in titles:
    i=i.text
    print(i)
