import os
from InquirerPy import prompt

ascii = """
\033[31m  _____    _            _    _____             _                    
\033[33m |_   _|  | |          | |  / ____|           | |                   
\033[32m   | |  __| | ___  __ _| | | |  __  __ _ ___  | |     __ ___      __
\033[36m   | | / _` |/ _ \/ _` | | | | |_ |/ _` / __| | |    / _` \ \ /\ / /
\033[34m  _| || (_| |  __/ (_| | | | |__| | (_| \__ \ | |___| (_| |\ V  V / 
\033[35m |_____\__,_|\___|\__,_|_|  \_____|\__,_|___/ |______\__,_| \_/\_/     \033[37m                                                                                                                                                                                                                                                                                                   
"""

def art_ascii():
    os.system("cls" if os.name == "nt" else "clear")
    print(ascii)

def error_log(log_message: str) -> None:
    os.system("cls" if os.name == "nt" else "clear")
    print(f'\033[91m{log_message}')

def back_log():

    def return_app():
        pass

    options = {
        "Return": return_app,
        "Exit": exit,
    }

    questions = [
        {
            "type": "list",
            "message": "Return or Exit",
            "choices": list(options.keys()),
            "name": "option",
        }
    ]
    
    answers = prompt(questions)

    select_func = options[answers['option']]
    select_func()

def home_log():
    art_ascii()
    print("\033[34mDeveloper By Narngisa (Github: Narngisa)\n\033[32mSupport me: \033[35mhttps://ko-fi.com/narngisa\033[37m")

    options = {
        "Yes": True,
        "No": exit,
    }

    questions = [
        {
            "type": "list",
            "message": "Will you start app?",
            "choices": list(options.keys()),
            "name": "option",
        }
    ]
    
    answers = prompt(questions)

    select_func = options[answers['option']]

    return select_func

def choice_func():
    art_ascii()

    options = {
        "PV = nRT": 0,
        "PV = g/MwRT": 1,
        "PMw = DRT": 2,
        "P = MRT": 3,
    }

    questions = [
        {
            "type": "list",
            "message": "Choose a function to calculate. ",
            "choices": list(options.keys()),
            "name": "option",
        }
    ]
    
    func_cal = prompt(questions)

    choice = options[func_cal['option']]

    return choice

def calculate_std():
    art_ascii()

    options = {
        "Pressure": 0,
        "Volume": 1,
        "Mol": 2,
        "Temperature": 3,
    }

    questions = [
        {
            "type": "list",
            "message": "Choose a function to calculate. ",
            "choices": list(options.keys()),
            "name": "option",
        }
    ]
    
    choice_cal = prompt(questions)

    cal = options[choice_cal['option']]
    
    return cal

def calculate_mw():
    art_ascii()

    options = {
        "Pressure": 0,
        "Volume": 1,
        "Grams / Molecular Weight": 2,
        "Temperature": 3,
    }

    questions = [
        {
            "type": "list",
            "message": "Choose a function to calculate. ",
            "choices": list(options.keys()),
            "name": "option",
        }
    ]
    
    choice_cal = prompt(questions)

    cal = options[choice_cal['option']]

    return cal

def calculate_d():
    art_ascii()

    options = {
        "Pressure": 0,
        "Molecular Weight": 1,
        "Density": 2,
        "Temperature": 3,
    }

    questions = [
        {
            "type": "list",
            "message": "Choose a function to calculate. ",
            "choices": list(options.keys()),
            "name": "option",
        }
    ]
    
    choice_cal = prompt(questions)

    cal = options[choice_cal['option']]

    return cal

def calculate_mo():
    art_ascii()

    options = {
        "Pressure": 0,
        "Molar": 1,
        "Temperature": 2,
    }

    questions = [
        {
            "type": "list",
            "message": "Choose a function to calculate. ",
            "choices": list(options.keys()),
            "name": "option",
        }
    ]
    
    choice_cal = prompt(questions)

    cal = options[choice_cal['option']]

    return cal
