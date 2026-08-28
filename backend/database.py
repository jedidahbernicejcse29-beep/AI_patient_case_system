import sqlite3
import os


DATABASE = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "patients.db"
)


# =========================
# CREATE DATABASE
# =========================

def create_database():

    connection = sqlite3.connect(DATABASE)

    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS patients (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            age TEXT,
            gender TEXT,
            chief_complaint TEXT,
            duration TEXT,
            symptoms TEXT,
            medical_history TEXT,
            surgical_history TEXT,
            medications TEXT,
            allergies TEXT,
            family_history TEXT,
            personal_history TEXT
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS ayush_history (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            patient_id INTEGER,
            prakriti TEXT,
            vikriti TEXT,
            sara TEXT,
            samhanana TEXT,
            pramana TEXT,
            satmya TEXT,
            sattva TEXT,
            ahara_shakti TEXT,
            vyayama_shakti TEXT,
            vaya TEXT,
            FOREIGN KEY(patient_id)
                REFERENCES patients(id)
        )
    """)

    connection.commit()
    connection.close()


# =========================
# SAVE PATIENT
# =========================

def save_patient(patient):

    connection = sqlite3.connect(DATABASE)

    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO patients (
            name,
            age,
            gender,
            chief_complaint,
            duration,
            symptoms,
            medical_history,
            surgical_history,
            medications,
            allergies,
            family_history,
            personal_history
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        patient.get("name", ""),
        patient.get("age", ""),
        patient.get("gender", ""),
        patient.get("chief_complaint", ""),
        patient.get("duration", ""),
        patient.get("symptoms", ""),
        patient.get("medical_history", ""),
        patient.get("surgical_history", ""),
        patient.get("medications", ""),
        patient.get("allergies", ""),
        patient.get("family_history", ""),
        patient.get("personal_history", "")
    ))

    patient_id = cursor.lastrowid

    connection.commit()
    connection.close()

    return patient_id


# =========================
# SAVE AYUSH
# =========================

def save_ayush(patient_id, ayush):

    connection = sqlite3.connect(DATABASE)

    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO ayush_history (
            patient_id,
            prakriti,
            vikriti,
            sara,
            samhanana,
            pramana,
            satmya,
            sattva,
            ahara_shakti,
            vyayama_shakti,
            vaya
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        patient_id,
        ayush.get("prakriti", ""),
        ayush.get("vikriti", ""),
        ayush.get("sara", ""),
        ayush.get("samhanana", ""),
        ayush.get("pramana", ""),
        ayush.get("satmya", ""),
        ayush.get("sattva", ""),
        ayush.get("ahara_shakti", ""),
        ayush.get("vyayama_shakti", ""),
        ayush.get("vaya", "")
    ))

    connection.commit()
    connection.close()


# =========================
# GET PATIENTS
# =========================

def get_patients():

    connection = sqlite3.connect(DATABASE)

    connection.row_factory = sqlite3.Row

    cursor = connection.cursor()

    cursor.execute("""
        SELECT *
        FROM patients
        ORDER BY id DESC
    """)

    patients = cursor.fetchall()

    connection.close()

    return patients


# =========================
# GET AYUSH HISTORY
# =========================

def get_ayush_history():

    connection = sqlite3.connect(DATABASE)

    connection.row_factory = sqlite3.Row

    cursor = connection.cursor()

    cursor.execute("""
        SELECT *
        FROM ayush_history
        ORDER BY id DESC
    """)

    history = cursor.fetchall()

    connection.close()

    return history