
from flask import Flask, render_template, request
import os
import sys

from werkzeug.utils import secure_filename
from PIL import Image
import pytesseract


# ============================================================
# CONNECT TO ai_model
# ============================================================

PROJECT_FOLDER = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)

sys.path.append(PROJECT_FOLDER)

from ai_model.clinical_model import analyze_patient


# ============================================================
# DATABASE
# ============================================================

from database import (
    create_database,
    save_patient,
    get_patients,
    save_ayush,
    get_ayush_history
)


# ============================================================
# FLASK
# ============================================================

app = Flask(__name__)


# ============================================================
# UPLOAD FOLDER
# ============================================================

UPLOAD_FOLDER = os.path.join(
    os.path.dirname(__file__),
    "uploads"
)

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

os.makedirs(
    UPLOAD_FOLDER,
    exist_ok=True
)


# ============================================================
# TESSERACT
# ============================================================

pytesseract.pytesseract.tesseract_cmd = (
    r"C:\Program Files\Tesseract-OCR\tesseract.exe"
)


# ============================================================
# ALLOWED FILES
# ============================================================

ALLOWED_EXTENSIONS = {
    "png",
    "jpg",
    "jpeg",
    "pdf"
}


def allowed_file(filename):

    return (
        "." in filename
        and
        filename.rsplit(".", 1)[1].lower()
        in ALLOWED_EXTENSIONS
    )


# ============================================================
# OCR DETAIL EXTRACTION
# ============================================================

def extract_patient_details(text):

    patient = {

        "name": "",

        "age": "",

        "gender": "",

        "chief_complaint": "",

        "duration": "",

        "symptoms": ""
    }


    lines = text.splitlines()


    for line in lines:

        line = line.strip()

        lower = line.lower()


        if lower.startswith("patient name:"):

            patient["name"] = (
                line.split(":", 1)[1].strip()
            )


        elif lower.startswith("name:"):

            patient["name"] = (
                line.split(":", 1)[1].strip()
            )


        elif lower.startswith("age:"):

            patient["age"] = (
                line.split(":", 1)[1].strip()
            )


        elif lower.startswith("gender:"):

            patient["gender"] = (
                line.split(":", 1)[1].strip()
            )


        elif lower.startswith("chief complaint:"):

            patient["chief_complaint"] = (
                line.split(":", 1)[1].strip()
            )


        elif lower.startswith("duration:"):

            patient["duration"] = (
                line.split(":", 1)[1].strip()
            )


        elif lower.startswith("symptoms:"):

            patient["symptoms"] = (
                line.split(":", 1)[1].strip()
            )


    return patient


# ============================================================
# HOME
# ============================================================

@app.route("/")
def home():

    return render_template(
        "index.html"
    )


# ============================================================
# PATIENT FORM
# ============================================================

@app.route(
    "/submit",
    methods=["POST"]
)
def submit():

    patient = {

        "name":
            request.form.get(
                "patient_name",
                ""
            ),

        "age":
            request.form.get(
                "age",
                ""
            ),

        "gender":
            request.form.get(
                "gender",
                ""
            ),

        "chief_complaint":
            request.form.get(
                "chief_complaint",
                ""
            ),

        "duration":
            request.form.get(
                "duration",
                ""
            ),

        "symptoms":
            request.form.get(
                "symptoms",
                ""
            ),

        "medical_history":
            request.form.get(
                "medical_history",
                ""
            ),

        "surgical_history":
            request.form.get(
                "surgical_history",
                ""
            ),

        "medications":
            request.form.get(
                "medications",
                ""
            ),

        "allergies":
            request.form.get(
                "allergies",
                ""
            ),

        "family_history":
            request.form.get(
                "family_history",
                ""
            ),

        "personal_history":
            request.form.get(
                "personal_history",
                ""
            )
    }


    return render_template(
        "questions.html",
        patient=patient
    )


# ============================================================
# GUIDED QUESTIONS + AI ANALYSIS
# ============================================================

@app.route(
    "/questions",
    methods=["POST"]
)
def questions():

    patient = {

        "name":
            request.form.get(
                "name",
                ""
            ),

        "age":
            request.form.get(
                "age",
                ""
            ),

        "gender":
            request.form.get(
                "gender",
                ""
            ),

        "chief_complaint":
            request.form.get(
                "chief_complaint",
                ""
            ),

        "duration":
            request.form.get(
                "duration",
                ""
            ),

        "symptoms":
            request.form.get(
                "symptoms",
                ""
            ),

        "medical_history":
            request.form.get(
                "medical_history",
                ""
            ),

        "surgical_history":
            request.form.get(
                "surgical_history",
                ""
            ),

        "medications":
            request.form.get(
                "medications",
                ""
            ),

        "allergies":
            request.form.get(
                "allergies",
                ""
            ),

        "family_history":
            request.form.get(
                "family_history",
                ""
            ),

        "personal_history":
            request.form.get(
                "personal_history",
                ""
            ),

        "onset":
            request.form.get(
                "onset",
                ""
            ),

        "severity":
            request.form.get(
                "severity",
                ""
            ),

        "associated_symptoms":
            request.form.get(
                "associated_symptoms",
                ""
            ),

        "factors":
            request.form.get(
                "factors",
                ""
            )
    }


    # ========================================================
    # AI MODEL
    # ========================================================

    ai_result = analyze_patient(
        patient
    )


    patient["ai_priority"] = (
        ai_result["priority"]
    )

    patient["ai_red_flags"] = (
        ai_result["red_flags"]
    )

    patient["ai_symptoms"] = (
        ai_result["symptoms"]
    )


    # ========================================================
    # SAVE PATIENT
    # ========================================================

    patient_id = save_patient(
        patient
    )


    patient["patient_id"] = patient_id


    # ========================================================
    # RED FLAG STATUS
    # ========================================================

    patient["red_flag"] = bool(
        ai_result["red_flags"]
    )


    return render_template(
        "summary.html",
        patient=patient
    )


# ============================================================
# PATIENT + AYUSH RECORDS
# ============================================================

@app.route("/records")
def records():

    patients = get_patients()

    history = get_ayush_history()


    return render_template(

        "records.html",

        patients=patients,

        history=history

    )


# ============================================================
# AYUSH FORM
# ============================================================

@app.route(
    "/ayush",
    methods=["GET", "POST"]
)
def ayush():

    if request.method == "POST":

        ayush_data = {

            "prakriti":
                request.form.get(
                    "prakriti",
                    ""
                ),

            "vikriti":
                request.form.get(
                    "vikriti",
                    ""
                ),

            "sara":
                request.form.get(
                    "sara",
                    ""
                ),

            "samhanana":
                request.form.get(
                    "samhanana",
                    ""
                ),

            "pramana":
                request.form.get(
                    "pramana",
                    ""
                ),

            "satmya":
                request.form.get(
                    "satmya",
                    ""
                ),

            "sattva":
                request.form.get(
                    "sattva",
                    ""
                ),

            "ahara_shakti":
                request.form.get(
                    "ahara_shakti",
                    ""
                ),

            "vyayama_shakti":
                request.form.get(
                    "vyayama_shakti",
                    ""
                ),

            "vaya":
                request.form.get(
                    "vaya",
                    ""
                )
        }


        # ====================================================
        # GET LATEST PATIENT
        # ====================================================

        patients = get_patients()


        if patients:

            patient_id = patients[0]["id"]

            save_ayush(
                patient_id,
                ayush_data
            )


        return render_template(

            "ayush_summary.html",

            ayush=ayush_data

        )


    return render_template(
        "ayush.html"
    )


# ============================================================
# AYUSH RECORDS
# ============================================================

@app.route("/ayush_records")
def ayush_records():

    history = get_ayush_history()


    return render_template(

        "ayush_records.html",

        history=history

    )


# ============================================================
# UPLOAD MEDICAL DOCUMENT
# ============================================================

@app.route(
    "/upload",
    methods=["GET", "POST"]
)
def upload():

    if request.method == "POST":


        if "document" not in request.files:

            return "No document selected"


        file = request.files["document"]


        if file.filename == "":

            return "No document selected"


        if not allowed_file(
            file.filename
        ):

            return "File type not allowed"


        filename = secure_filename(
            file.filename
        )


        file_path = os.path.join(

            app.config[
                "UPLOAD_FOLDER"
            ],

            filename

        )


        file.save(
            file_path
        )


        extracted_text = ""


        # ====================================================
        # IMAGE OCR
        # ====================================================

        if filename.lower().endswith(

            (
                ".png",
                ".jpg",
                ".jpeg"
            )

        ):

            image = Image.open(
                file_path
            )


            extracted_text = (

                pytesseract.image_to_string(
                    image
                )

            )


            extracted_text = "\n".join(

                line.strip()

                for line
                in extracted_text.splitlines()

                if line.strip()

            )


        # ====================================================
        # PDF
        # ====================================================

        elif filename.lower().endswith(
            ".pdf"
        ):

            extracted_text = (

                "PDF uploaded successfully.\n\n"

                "PDF text extraction will "
                "be added later."

            )


        # ====================================================
        # EXTRACT PATIENT DETAILS
        # ====================================================

        patient = extract_patient_details(
            extracted_text
        )


        # ====================================================
        # OCR RESULT
        # ====================================================

        return render_template(

            "ocr_result.html",

            filename=filename,

            extracted_text=extracted_text,

            patient=patient

        )


    return render_template(
        "upload.html"
    )


# ============================================================
# OCR → PATIENT FORM
# ============================================================

@app.route(
    "/ocr_to_form",
    methods=["POST"]
)
def ocr_to_form():

    patient = {

        "name":
            request.form.get(
                "patient_name",
                ""
            ),

        "age":
            request.form.get(
                "age",
                ""
            ),

        "gender":
            request.form.get(
                "gender",
                ""
            ),

        "chief_complaint":
            request.form.get(
                "chief_complaint",
                ""
            ),

        "duration":
            request.form.get(
                "duration",
                ""
            ),

        "symptoms":
            request.form.get(
                "symptoms",
                ""
            ),

        "medical_history": "",

        "surgical_history": "",

        "medications": "",

        "allergies": "",

        "family_history": "",

        "personal_history": ""
    }


    return render_template(

        "index.html",

        patient=patient

    )


# ============================================================
# CREATE DATABASE
# ============================================================

create_database()


# ============================================================
# START APPLICATION
# ============================================================

if __name__ == "__main__":

    app.run(
        debug=True
    )

