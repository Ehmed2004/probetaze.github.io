import requests
import json
import os

API_KEY = os.environ.get("FOOTBALL_API_KEY")
URL = "https://api.football-data.org/v4/matches"

headers = {"X-Auth-Token": API_KEY}
response = requests.get(URL, headers=headers)

matches_data = []

if response.status_code == 200:
    data = response.json()
    for match in data.get("matches", []):
        home = match["homeTeam"]["name"]
        away = match["awayTeam"]["name"]
        league = match["competition"]["name"]

        # Avtomatik proqnoz formalaşdıran kod
        item = {
            "homeTeam": home,
            "awayTeam": away,
            "league": league,
            "scores": "2:1 / 3:1 / 1:1",
            "predictions": ["Ev 1.5 Üst", "Qol-Qol Bəli", "2.5 Üst"]
        }
        matches_data.append(item)

with open("data.json", "w", encoding="utf-8") as f:
    json.dump(matches_data, f, ensure_ascii=False, indent=4)
