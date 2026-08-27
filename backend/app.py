from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/submit", methods=["POST"])
def submit():

    patient = {
        "name": request.form.get("patient_name"),
        "age": request.form.get("age"),
        "gender": request.form.get("gender"),
        "chief_complaint": request.form.get("chief_complaint"),
        "duration": request.form.get("duration"),
        "symptoms": request.form.get("symptoms"),
        "medical_history": request.form.get("medical_history"),
        "surgical_history": request.form.get("surgical_history"),
        "medications": request.form.get("medications"),
        "allergies": request.form.get("allergies"),
        "family_history": request.form.get("family_history"),
        "personal_history": request.form.get("personal_history")
    }

    return render_template("summary.html", patient=patient)


if __name__ == "__main__":
    app.run(debug=True)