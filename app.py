from utils.logger import *
from utils.std_gas import *
from utils.mw_gas import *

from InquirerPy import prompt

def home():
    art_ascii()

    options = {
        "PV = nRT": 0,
        "PV = g/MwRT": 1,
        "PM = DRT": back_log,
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
    
    if choice == 0:
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

        calculate = options[choice_cal['option']]

        if calculate == 0:
            std_p()
        elif calculate == 1:
            std_v()
        elif calculate == 2:
            std_n()
        elif calculate == 3:
            std_t()
    
    elif choice == 1:
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

        calculate = options[choice_cal['option']]

        if calculate == 0:
            mw_p()
        elif calculate == 1:
            mw_v()
        elif calculate == 2:
            mw_mw()
        elif calculate == 3:
            mw_t()

    print("\n")
    back_log()
