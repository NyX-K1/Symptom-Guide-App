import display
import symptom_data
import triage_logic

def main() : 
    display.print_welcome()
    while True : 
        display.main_menu(symptom_data.symptom_tree)
        choice = input("Enter a SYMPTOM or 'q' To Quit : ").lower()
        if choice == 'q' :
            display.good_bye()
            break
        elif choice in symptom_data.symptom_tree :
            start_node = symptom_data.symptom_tree[choice]
            triage_logic.walk_tree(start_node)
        else : 
            display.print_invalid_choice()

if __name__ == "__main__":
    main()
