import os

def clear_screen() : 
    if (os.name == "nt") : 
        os.system('cls')
    else :
        os.system('clear')

def print_welcome() : 
    print(".........Welcome To Our SYMPTOMS GUIDE")
    print("This tool helps you to check in your common symptoms.")
    input("Press ENTER To Continue")

def main_menu(symptom_data) : 
    clear_screen()
    print("MAIN MENU")
    symptoms = list(symptom_data.keys())
    for i,symptom in enumerate(symptoms) : 
        print(f" {i+1}. {symptom.capitalize()}")
    print("\nType 'q' to QUIT")

def good_bye() :
    clear_screen
    print("THANK YOU for using Symptom Guide. Hope we helped you!!!! STAY HEALTHY")

def print_invalid_choice() :
    print("\n Invalid Choice!?! Please Try Again.")
    input("Press ENTER To Continue")

def print_question(question_text) :
    print(f"❓ {question_text}")

def print_options(option_list) :
    for item in option_list : 
        print(f"- {item}")

def print_advice(advice_text) : 
    if ("RED FLAG" in advice_text) :
        print(f"🚨 {advice_text} 🚨")
    else : 
        print(f"💡 {advice_text}")
    input("Press ENTER To Return To MAIN MENU")
