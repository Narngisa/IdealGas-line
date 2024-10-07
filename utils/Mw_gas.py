from utils.logger import *

r = 0.0821

def mw_p():
    art_ascii()
    print("Function: PV = g/MwRT")
    volume = float(input("Volume: "))

    options_v = {
        "Cubic Centimeter or Milliliter": 0,
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
    print("Function: PV = g/MwRT")
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

    art_ascii()
    print("Function: PV = g/MwRT")

    molecular_weight = float(input("Molecular Weight: "))

    art_ascii()
    print("Function: PV = g/MwRT")
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
    print("Function: PV = g/MwRT")
    print("Calculate: Pressure")

    pressure = ((grams / molecular_weight)* r * temperature) / volume

    print(f"V = {volume} L\ng/Mw = {grams}/{molecular_weight} g/mol\nR = {r}\nT = {temperature} K\n\nP = {pressure:.2f} atm")

def mw_v():
    art_ascii()
    print("Function: PV = g/MwRT")
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
    print("Function: PV = g/MwRT")
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

    art_ascii()
    print("Function: PV = g/MwRT")

    molecular_weight = float(input("Molecular Weight: "))

    art_ascii()
    print("Function: PV = g/MwRT")
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
    print("Function: PV = g/MwRT")
    print("Calculate: Volume")

    volume = ((grams / molecular_weight) * r * temperature) / pressure

    print(f"P = {pressure} atm\ng/Mw = {grams}/{molecular_weight} g/mol\nR = {r}\nT = {temperature} K\n\nV = {volume:.2f} L")

def mw_mw():
    art_ascii()
    print("Function: PV = g/MwRT")
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
    print("Function: PV = g/MwRT")
    volume = float(input("Volume: "))

    options_v = {
        "Cubic Centimeter or Milliliter": 0,
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
    print("Function: PV = g/MwRT")
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
    print("Function: PV = g/MwRT")
    print("Calculate: Volume")

    grams_of_molecular_weight = (pressure * volume) / (r * temperature)

    print(f"P = {pressure} atm\nV = {volume:.2f} L \nR = {r}\nT = {temperature} K\n\ng/Mw = {grams_of_molecular_weight} g/mol")

def mw_t():
    art_ascii()
    print("Function: PV = g/MwRT")
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
    print("Function: PV = g/MwRT")
    volume = float(input("Volume: "))

    options_v = {
        "Cubic Centimeter or Milliliter": 0,
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
    print("Function: PV = g/MwRT")
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

    art_ascii()
    print("Function: PV = g/MwRT")

    molecular_weight = float(input("Molecular Weight: "))

    temperature = (pressure * volume) / ((grams / molecular_weight) * r)
    temperature_C = temperature - 273

    print(f"P = {pressure} atm\nV = {volume:.2f} L \nR = {r}\ng/Mw = {grams}/{molecular_weight} g/mol\n\nT = {temperature:.2f} K\nT = {temperature_C:.1f} C")
