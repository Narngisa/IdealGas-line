from utils.logger import *
from InquirerPy import prompt

r = 0.0821

def std_p():
    art_ascii()
    print("Function: PV = nRT")
    volume = float(input("Volume: "))

    options_v = {
        "Cubic Centimeters or Milliliter": 0,
        "Cubic Decimeter or Liter": 1,
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

    art_ascii()
    print("Function: PV = nRT")

    mol = float(input("Mol: "))

    art_ascii()
    print("Function: PV = nRT")
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

    art_ascii()
    print("Function: PV = nRT")
    print("Calculate: Pressure")

    pressure = (mol * r * temperature) / volume

    print(f"V = {volume} L\nn = {mol} mol\nR = {r}\nT = {temperature} K\n\nP = {pressure:.2f} atm")

def std_v():
    art_ascii()
    print("Function: PV = nRT")
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

    art_ascii()
    print("Function: PV = nRT")

    mol = float(input("Mol: "))

    art_ascii()
    print("Function: PV = nRT")
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

    art_ascii()
    print("Function: PV = nRT")
    print("Calculate: Volume")

    volume = (mol * r * temperature) / pressure

    print(f"P = {pressure} atm\nn = {mol} mol\nR = {r}\nT = {temperature} K\n\nV = {volume:.2f} L")

def std_n():
    art_ascii()
    print("Function: PV = nRT")
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

    art_ascii()
    print("Function: PV = nRT")
    volume = float(input("Volume: "))

    options_v = {
        "Cubic Centimeters or Milliliter": 0,
        "Cubic Decimeter or Liter": 1,
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

    art_ascii()
    print("Function: PV = nRT")
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

    art_ascii()
    print("Function: PV = nRT")
    print("Calculate: Mol")

    mol = (pressure * volume) / (r * temperature)

    print(f"P = {pressure} atm\nV = {volume} L\nR = {r}\nT = {temperature} K\n\nn = {mol:.2f} mol")

def std_t():
    art_ascii()
    print("Function: PV = nRT")
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

    art_ascii()
    print("Function: PV = nRT")
    volume = float(input("Volume: "))

    options_v = {
        "Cubic Centimeters or Milliliter": 0,
        "Cubic Decimeter or Liter": 1,
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

    art_ascii()
    print("Function: PV = nRT")

    mol = float(input("Mol: "))

    art_ascii()
    print("Function: PV = nRT")
    print("Calculate: Temperature")

    temperature = (pressure * volume) / (mol * r)
    temperature_C = temperature - 273

    print(f"P = {pressure} atm\nV = {volume} L\nR = {r}\nn = {mol} mol\n\nT = {temperature:.2f} K\nT = {temperature_C:.1f} C")