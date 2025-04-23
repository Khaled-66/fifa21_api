from flask import Flask, jsonify
import pandas as pd

app = Flask(__name__)
df = pd.read_csv("api/players21-data.csv",low_memory=False) 
players_by_id = df.set_index("ID").to_dict(orient="index") #key: player_id, value: player data

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

if __name__ == "__main__":
    app.run(debug=True)
