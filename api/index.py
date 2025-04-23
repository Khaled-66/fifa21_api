from flask import Flask, jsonify
import pandas as pd
import os

app = Flask(__name__)
app.config["JSONIFY_PRETTYPRINT_REGULAR"] = True
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
        return Response(
            json.dumps({"id": player_id, **player}, indent=2),
            mimetype='application/json'
        )
    else:
        return Response(
            json.dumps({"error": "Player not found"}, indent=2),
            mimetype='application/json',
            status=404
        )
