from flask import Flask, request, jsonify
import db

app = Flask(__name__)
db.init_db()

@app.route("/")
def home():
    return "🏠 Courier Clicker API работает!"

@app.route("/save", methods=["POST"])
def save_progress():
    data = request.get_json()
    user_id = data.get("user_id")
    money = data.get("money")
    speed = data.get("speed")
    assistants = data.get("assistants")
    assistant_cost = data.get("assistant_cost")

    if None in (user_id, money, speed, assistants, assistant_cost):
        return jsonify({"status": "error", "message": "Missing data"}), 400

    db.create_user(user_id)
    db.update_user(user_id, money, speed, assistants, assistant_cost)

    return jsonify({"status": "success", "message": "Progress saved!"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)
