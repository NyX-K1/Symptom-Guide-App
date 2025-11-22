# src/tests/test_triage.py
import sys
import os

import symptom_data

def run_tests():
    print("Starting Data Integrity Tests")
    
    # Test 1 - Checking if we have at least one symptom
    if len(symptom_data.symptom_tree) > 0:
        print("PASS: Symptom tree is not empty.")
    else:
        print("FAIL: Symptom tree is empty!")

    # Test 2 - Check a specific symptom (Fever)
    if "fever" in symptom_data.symptom_tree:
        print("PASS:'Fever' branch exists.")
        
        # Check if it has a question
        fever_node = symptom_data.symptom_tree["fever"]
        if "question" in fever_node :
             print(f"PASS: Fever has a starting question: '{fever_node['question'][:20]}'")
        else :
             print("FAIL: Fever is missing a question!")
    else :
        print("FAIL:'Fever' branch is missing!")

    print("\nAll Tests Completed")

if __name__ == "__main__":
    run_tests()