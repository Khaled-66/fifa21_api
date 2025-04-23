from flask import Flask, jsonify
import pandas as pd
import os

app = Flask(__name__)
csv_path = os.path.join(os.path.dirname(__file__), "players21-data.csv")
df = pd.read_csv(csv_path, low_memory=False)
players_by_id = df.set_index("ID").to_dict(orient="index")

@app.route("/")
def home():
    return jsonify({"message": "Welcome to the FIFA 21 API!"})

@app.route("/player/<int:player_id>", methods=["GET"])
def get_player(player_id):
    player = players_by_id.get(player_id)
    if player:
        return jsonify({"id": player_id, **player})
    else:
        return jsonify({"error": "Player not found"}), 404
