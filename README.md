\# Care AI



\## AI-Powered Patient Case Management System



Care AI is a team-based healthcare software project designed to organize patient case information, guided clinical history, AI-assisted clinical analysis, AYUSH assessments, medical document uploads, and patient records in one system.



> \*\*Note:\*\* The AI clinical analysis feature is a prototype for organizing clinical information and identifying predefined warning terms. It is not a medical diagnosis.



\---



\## Project Overview



Care AI provides a structured workflow for collecting and managing patient information.



The system allows users to:



\* Enter patient information

\* Collect guided clinical history

\* Perform prototype AI clinical analysis

\* Identify predefined red-flag terms

\* Store patient records

\* Complete AYUSH clinical assessments

\* View AYUSH records

\* Upload medical documents

\* Process supported medical documents

\* View information through a dashboard



\---



\## Main Features



\### Patient Case Taking



Collects basic patient information such as:



\* Name

\* Age

\* Gender

\* Chief complaint

\* Duration

\* Symptoms

\* Medical history

\* Surgical history

\* Medications

\* Allergies

\* Family history

\* Personal history



\### Guided Clinical History



Collects additional clinical information including:



\* Symptom onset

\* Severity

\* Associated symptoms

\* Factors affecting symptoms



\### AI Clinical Analysis



The prototype AI component analyzes entered clinical information and can identify predefined warning terms.



The system can provide:



\* Priority assessment

\* Detected red flags

\* Symptoms analyzed



\### AYUSH Module



Provides a structured Dashavidha Pariksha assessment containing:



1\. Prakriti

2\. Vikriti

3\. Sara

4\. Samhanana

5\. Pramana

6\. Satmya

7\. Sattva

8\. Ahara Shakti

9\. Vyayama Shakti

10\. Vaya



\### Medical Document Module



Supports uploading medical documents such as:



\* PDF

\* PNG

\* JPG

\* JPEG



\### Patient Records



Stores and displays submitted patient case information.



\### Dashboard



The Care AI dashboard provides:



\* Total patient count

\* AYUSH record count

\* Recent patient records

\* Quick actions

\* System modules

\* Navigation to major features



\---



\## Project Structure



```text

AI\_patient\_case\_system/

│

├── ai\_model/

│   ├── \_\_init\_\_.py

│   ├── clinical\_model.py

│   └── README.md

│

├── backend/

│   ├── app.py

│   ├── database.py

│   ├── templates/

│   │   ├── index.html

│   │   ├── questions.html

│   │   ├── summary.html

│   │   ├── records.html

│   │   ├── ayush.html

│   │   ├── ayush\_summary.html

│   │   ├── ayush\_records.html

│   │   ├── dashboard.html

│   │   ├── upload.html

│   │   ├── upload\_success.html

│   │   └── ocr\_result.html

│   └── uploads/

│

├── database/

│   └── database.py

│

├── frontend/

│   └── patient\_form.html

│

├── .gitignore

├── README.md

└── requirements.txt

```



\---



\## Technologies Used



\* Python

\* Flask

\* HTML

\* CSS

\* JavaScript

\* SQLite

\* Git

\* GitHub



\---



\## Running the Project



\### 1. Clone the repository



```bash

git clone <repository-url>

```



\### 2. Open the project



```bash

cd AI\_patient\_case\_system

```



\### 3. Install dependencies



```bash

pip install -r requirements.txt

```



\### 4. Run the Flask application



```bash

cd backend

python app.py

```



\### 5. Open the application



Open the following address in a browser:



```text

http://127.0.0.1:5000/

```



\---



\## GitHub Collaboration



The project uses Git and GitHub for team collaboration.



Team members work on separate branches and can submit Pull Requests to merge completed work into the main project.



Example:



```bash

git checkout -b feature-name

git add .

git commit -m "Add feature"

git push origin feature-name

```



\---



\## Project Status



\### Core Features Completed



\* Patient case-taking

\* Guided clinical history

\* AI clinical analysis prototype

\* Red-flag detection

\* Patient records

\* AYUSH assessment

\* AYUSH records

\* Medical document upload

\* Dashboard

\* GitHub collaboration structure



The project can be further extended with additional AI capabilities, authentication, advanced document processing, and external healthcare-system integrations.



\---



\## Disclaimer



Care AI is an educational/team software project. Its AI functionality is a prototype and should not be used as a substitute for professional medical diagnosis, treatment, or clinical decision-making.





