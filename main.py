from utils.logger import *
from app import *
from InquirerPy import prompt

def tool():
    art_ascii()
    print("\033[34mDeveloper By Narngisa\n\033[32mGithub: \033[35mhttps://github.com/Narngisalnw\033[37m")

    options = {
        "Yes": home,
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

    selected_function = options[answers['option']]
    selected_function()

if __name__ == "__main__":
    tool()