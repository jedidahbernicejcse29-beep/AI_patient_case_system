from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/")
def home():
    return jsonify({
        "message": "MediKiosk Backend is running"
    })


@app.route("/patient", methods=["POST"])
def patient():
    data = request.get_json()

    name = data.get("name")
    age = data.get("age")
    gender = data.get("gender")
    symptoms = data.get("symptoms")

    return jsonify({
        "message": "Patient information received",
        "patient": {
            "name": name,
            "age": age,
            "gender": gender,
            "symptoms": symptoms
        }
    })


if __name__ == "__main__":
    app.run(debug=True)
