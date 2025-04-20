
import requests

api_key = "68049477e6ef86501625d668"
url = "https://api.scrapingdog.com/linkedin"

params = {
    "api_key": api_key,
    "type": "profile",
    "linkId": "https://www.linkedin.com/in/sudoyolo",
    "private": "false"
}

response = requests.get(url, params=params)

if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print(f"Request failed with status code: {response.status_code}")