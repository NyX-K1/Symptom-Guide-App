Symptom Guide (Community Health Helper).

Overview of the Project.

Symptom Guide is a lightweight offline-first Python application designed to assist the community health workers and rural public. It provides a “triage logic tree” to assess a common symptom-fever, cough, headache-and flags possible “Red Flags” , while providing safe, pre-vetted advice.

✨ Features.
The Interactive Triage System is a question and answer flow that updates depending on user answers.
* It automatically flags potentially dangerous symptoms such as a stiff neck with fever and indicates immediate medical attention.

* It runs fully offline without an Internet connection - totally local.
* The logic is separated from data meaning it is easy to add new symptoms.

Technologies Used permalink ×.
* **Language:** Python 3.x.
* Libraries: Standard Library (os, sys) - no dependencies required.

???? How to Install & Run.
1. **Clone the Repository:**.
```bash.
git clone https://github.com/NyX-K1/Symptom-Guide.git.
cd Symptom-Guide.
```.
2. **Run the Application:**.

Go to the project folder and execute the main script.
```bash.
Run automated test script to check integrity of symptom data and logic, for testing run below in bash: ```bash python src/tests/test_triage.py
