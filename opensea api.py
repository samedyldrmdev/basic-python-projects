import requests

url = "https://testnets-api.opensea.io/api/v1/events?only_opensea=false&limit=20"

headers = {"Accept": "application/json"}
# event_type = "succesful"
response = requests.get(url, headers=headers)
print(response.text)
# print(succesful)
twitter = ""

for i in response.text:
    if "twitter.com" in response.text:
        twitter = i + twitter
        print(twitter)

# print(response.text.find("twitter"))