import requests

url = "https://testnets-api.opensea.io/api/v1/events?only_opensea=false&limit=20"

headers = {"Accept": "application/json"}
response = requests.get(url, headers=headers)
print(response.text)
