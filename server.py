from flask import Flask, request, jsonify

app = Flask(__name__)

# Fake database
EMPLOYEES = {
    "A1B2C3D4": "ALLOW",
    "11112222": "DENY"
}

@app.route("/attendance", methods=["POST"])
def attendance():
    data = request.json
    uid = data.get("rfid_uid")

    result = "ALLOW" if uid == "A1B2C3D4" else "DENY"

    return jsonify({"result": result})

if __name__ == "__main__":
    app.run()

