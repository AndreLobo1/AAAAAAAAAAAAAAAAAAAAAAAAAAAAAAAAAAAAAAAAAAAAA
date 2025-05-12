# src/utils/utils.py

def input_with_prompt(prompt, error_msg=""):
    while True:
        user_input = input(prompt).strip()
        if user_input:
            return user_input
        else:
            print(error_msg)

def clear_screen():
    import os
    os.system('cls' if os.name == 'nt' else 'clear')