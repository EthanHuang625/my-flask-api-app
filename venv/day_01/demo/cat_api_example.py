import requests

# https://catfact.ninja/

url = "https://catfact.ninja/fact"
response = requests.get(url)
print (response.status_code)
data = response.json()

print("Random Cat Fact:", data["fact"])
