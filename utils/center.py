from utils.logger import *
from InquirerPy import prompt

def pressure_cal(message: str) -> None:
    art_ascii()
    print(f"Function: {message}")
    pressure = float(input("Pressure: "))

    options_p = {
        "mmHg or Torr": 0,
        "psi": 1,
        "atm": 2,
    }

    questions_p = [
        {
            "type": "list",
            "message": "Choose value of pressure?",
            "choices": list(options_p.keys()),
            "name": "option",
        }
    ]
    
    answers_p = prompt(questions_p)

    value_p = options_p[answers_p['option']]

    if value_p == 0:
        pressure = pressure / 760
    elif value_p == 1:
        pressure = pressure / 14.69
    elif value_p == 3:
        pass
    
    return pressure

def volume_cal(message: str) -> None:
    art_ascii()
    print(f"Function: {message}")
    volume = float(input("Volume: "))

    options_v = {
        "Milliliter or Cubic Centimeters": 0,
        "Liter or Cubic Decimeter": 1,
    }

    questions_v = [
        {
            "type": "list",
            "message": "Choose value of volume?",
            "choices": list(options_v.keys()),
            "name": "option",
        }
    ]
    
    answers_v = prompt(questions_v)

    value_v = options_v[answers_v['option']]

    if value_v == 0:
        volume = volume / 1000
    elif value_v == 1:
        pass

    return volume

def mol_cal(message: str) -> None:
    art_ascii()
    print(f"Function: {message}")
    mol = float(input("Mol: "))

    return mol

def temperature_cal(message: str) -> None:
    art_ascii()
    print(f"Function: {message}")
    temperature = float(input("Temperature: "))

    options_t = {
        "Celsius": 0,
        "Kelvin": 1,
    }

    questions_t = [
        {
            "type": "list",
            "message": "Choose value of temperature?",
            "choices": list(options_t.keys()),
            "name": "option",
        }
    ]
    
    answers_t = prompt(questions_t)

    value_t = options_t[answers_t['option']]

    if value_t == 0:
        temperature = temperature + 273
    elif value_t == 1:
        pass

    return temperature

def grams_cal(message: str) -> None:
    art_ascii()
    print(f"Function: {message}")
    grams = float(input("Grams: "))

    options_g = {
        "Kilograms": 0,
        "Grams": 1,
    }

    questions_g = [
        {
            "type": "list",
            "message": "Choose value of grams?",
            "choices": list(options_g.keys()),
            "name": "option",
        }
    ]
    
    answers_g = prompt(questions_g)

    value_g = options_g[answers_g['option']]

    if value_g == 0:
        grams = grams * 1000
    elif value_g == 1:
        pass

    return grams

def molecular_weight_cal(message: str) -> None:
    art_ascii()
    print(f"Function: {message}")
    molecular_weight = float(input("Molecular Weight: "))

    return molecular_weight

def density_cal(message: str) -> None:
    art_ascii()
    print(f"Function: {message}")
    density = float(input("Density: "))

    return density

def molar_cal(message: str) -> None:
    art_ascii()
    print(f"Function: {message}")
    molar = float(input("Molar: "))

    return molar