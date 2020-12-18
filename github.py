import requests

username = "BairBuyrchiyev"
personalaccesstoken = open("token.txt", "r")
response = requests.get("https://api.github.com/users/BairBuyrchiyev/repos", auth = (username, personalaccesstoken))
print(response.text)