import json
import requests

url = "https://americas.api.riotgames.com/lol/match/v5/matches/NA1_4639488107"
headers = {"X-Riot-Token": "RGAPI-a7493dd6-4dc4-4f2e-9f3a-e698ab203b0f"}
response = requests.get(url, headers=headers)
data = response.json()
formatted_response = json.dumps(data, indent=4)
print(formatted_response)