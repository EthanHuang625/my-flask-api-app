from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Welcome to My Flask API App!</h1>"

@app.route("/football-info")
def football_info():
    url = "https://api-football-standings.azharimm.site/leagues"
    response = requests.get(url)
    data = response.json()
    Info = {
        "name": "English Premier League",
        "abbreviation": "Prem",
        "seasonDisplay": "2020-2021",
        "season": 2020,
        "standings": [data]
    }
    return jsonify(Info)

if __name__ == "__main__":
    app.run(debug=True) 

