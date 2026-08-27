from flask import Blueprint, request, jsonify

patient_routes = Blueprint("patient_routes", __name__)

@patient_routes.route("/patient", methods=["POST"])
def add_patient():
    data = request.get_json()

    return jsonify({
        "message": "Patient added successfully",
        "data": data
    })