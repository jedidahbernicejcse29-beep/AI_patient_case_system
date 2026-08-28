
# MediKiosk AI Clinical Analysis
# Prototype decision-support module


def analyze_patient(patient):

    complaint = (
        patient.get("chief_complaint", "")
        or ""
    ).lower()

    symptoms = (
        patient.get("symptoms", "")
        or ""
    ).lower()

    associated = (
        patient.get("associated_symptoms", "")
        or ""
    ).lower()


    text = (
        complaint
        + " "
        + symptoms
        + " "
        + associated
    )


    red_flags = [
        "chest pain",
        "difficulty breathing",
        "severe breathing",
        "fainting",
        "sudden weakness"
    ]


    detected_flags = []


    for flag in red_flags:

        if flag in text:

            detected_flags.append(flag)


    if detected_flags:

        priority = "Priority assessment recommended"

    else:

        priority = "Routine assessment"


    return {

        "priority": priority,

        "red_flags": detected_flags,

        "symptoms": text.strip()
    }

