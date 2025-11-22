Project Definition.

1. Problem Statement.


In low-resource rural or community settings, problems that prevent people and community health workers from accessing reliable, simple, and offline health information are commonplace. When a fever or cough occurs, it is usually hard to know what questions to ask, what “red flag” signs to look for, or when to get professional advice.  The outcome can be panic or worse, a delay in seeking essential medical attention.

Solution: The “Symptom Guide” is a simple and 100% offline text-based application. Which is based on Python programming language. It comes with a guided “triage logic tree” that will take a user through a series of simple questions about a main symptom. It may not be able to provide diagnosis but it will help the user identify possible red flags and offer safe, pre-vetted advice that can help inform decisions.


2. Project Scope.


The scope of this project will be limited to.
* A Python console application that works offline.
A logic engine, which follows rules helps to navigate a symptom tree. The Navigating is done using nested dictionaries in Python.
* Providing lists of things to watch and things to know, not medical diagnoses.
* A text-based interface that is navigated using simple text inputs is termed TUI.

* The project will not be connected to any APIs, databases or the internet.
* The project won't collect any user data or personal health information.


3. Target Users.


* Community health workers professionals in the field who need quick and dependable offline support to help them ask consistent and safe questions while visiting homes for health check-ups.
* In a home setting, these are the people that have to assess a family member’s symptoms and assess the best next course of action like resting at home versus going to a clinic.
* People who cannot access online health symptom checkers reliably due to poor internet access.

  
4. High-Level Features.


* The primary menu through which the user can perform a clear selection of a chief symptom like 'fever', 'cough', ‘headache’ etc.
* Guided triage logic is a question-and-answer flow that guides the user along a decision tree based on their inputs.
* Identifying red flags: The system detects and indicates when someone has answered items indicating that they might have a stiff neck, difficulty breathing, etc.
* The system offers a straightforward summary, at the end of a logic path, such as Advice: Rest and hydrate, or Recommendation: See a doctor.
* Offline Features: The entire application and all data reside on the machine it is running without requiring any Internet access whatsoever.
