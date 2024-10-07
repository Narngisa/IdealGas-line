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
        os.system("python main.py")

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

    selected_function = options[answers['option']]
    selected_function()