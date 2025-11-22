import display

def walk_tree(current_node) : 
    while True : 
        if ("question" in current_node) : 
            display.print_question(current_node["question"])
            option_list = list(current_node["options"].keys())
            display.print_options(option_list)
            user_response = input("Enter your response : ").lower()
            if(user_response in option_list) : 
                current_node = current_node["options"][user_response]
            else : 
                display.print_invalid_choice()
        elif ("advice" in current_node) : 
            display.print_advice(current_node["advice"])
            break
        else : 
            print("Invalid Node Data")
            break
