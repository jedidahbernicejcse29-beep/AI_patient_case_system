from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/submit", methods=["POST"])
def submit():
    name = request.form["patient_name"]
    age = request.form["age"]
    symptoms = request.form["symptoms"]

    return f"""
    <h1>Patient Details</h1>
    <p>Name: {name}</p>
    <p>Age: {age}</p>
    <p>Symptoms: {symptoms}</p>
    """

if __name__ == "__main__":
    app.run(debug=True)