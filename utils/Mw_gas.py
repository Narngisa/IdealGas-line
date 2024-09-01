from utils.logger import *

r = 0.0821

def Mw_p():

    clear_log()
    art_ascii()
    ideal_molecular()
    volume = float(input("V: "))

    if volume == 0:
        clear_log()
        error_log("Error: Zero number cannot calculate !!")
        back_log()
    else:
        pass

    clear_log()
    art_ascii()
    ideal_molecular()
    print("[0] cm^3\n[1] dm^3 or L")
    unit_v = int(input("\n>> "))

    if unit_v == 0:
        volume = volume / 1000
    elif unit_v == 1:
        pass
    else: 
        error_log(f"Error: No value in function !!")
        back_log()

    clear_log()
    art_ascii()
    ideal_molecular()
    print("Input mass of gas")
    grams = float(input("g: "))

    clear_log()
    art_ascii()
    ideal_molecular()
    print("[0] kg\n[1] g")
    unit_g = int(input("\n>> "))

    if unit_g == 0:
        grams = grams * 1000
    elif unit_g == 1:
        pass
    else: 
        error_log(f"Error: No value in function !!")
        back_log()

    clear_log()
    art_ascii()
    ideal_molecular()
    print("Input molecular mass of gas")
    molecular_mass = float(input("Mw: "))

    clear_log()
    art_ascii()
    ideal_molecular()
    temperature = float(input("T: "))

    clear_log()
    art_ascii()
    ideal_molecular()
    print("[0] C\n[1] K")
    unit_t = int(input("\n>> "))

    if unit_t == 0:
        temperature = temperature + 273
    elif unit_t == 1:
        pass
    else: 
        error_log(f"Error: No value in function !!")
        back_log()
    
    clear_log()
    art_ascii()
    ideal_molecular()
    cal_p()

    pressure = ((grams / molecular_mass)* r * temperature) / volume

    print(f"V = {volume} L\ng/Mw = {grams}/{molecular_mass} \nR = {r}\nT = {temperature} K\n\nP = {pressure:.2f} atm")

def Mw_v():

    clear_log()
    art_ascii()
    ideal_molecular()
    pressure = float(input("P: "))

    if pressure == 0:
        clear_log()
        error_log("Error: Zero number cannot calculate !!")
        back_log()
    else:
        pass

    clear_log()
    art_ascii()
    ideal_molecular()
    print("[0] mmHg or Torr\n[1] psi\n[2] atm")
    
    unit_p = int(input("\n>> "))

    if unit_p == 0:
        pressure = pressure / 760
    elif unit_p == 1:
        pressure = pressure / 14.69
    elif unit_p == 2:
        pass
    else: 
        error_log("Error: No value in function !!")
        back_log()

    clear_log()
    art_ascii()
    ideal_molecular()
    print("Input mass of gas")
    grams = float(input("g: "))

    clear_log()
    art_ascii()
    ideal_molecular()
    print("[0] kg\n[1] g")
    unit_g = int(input("\n>> "))

    if unit_g == 0:
        grams = grams * 1000
    elif unit_g == 1:
        pass
    else: 
        error_log(f"Error: No value in function !!")
        back_log()

    clear_log()
    art_ascii()
    ideal_molecular()
    print("Input molecular mass of gas")
    molecular_mass = float(input("Mw: "))

    clear_log()
    art_ascii()
    ideal_molecular()
    temperature = float(input("T: "))

    clear_log()
    art_ascii()
    ideal_molecular()
    print("[0] C\n[1] K")
    unit_t = int(input("\n>> "))

    if unit_t == 0:
        temperature = temperature + 273
    elif unit_t == 1:
        pass
    else: 
        error_log(f"Error: No value in function !!")
        back_log()
    
    clear_log()
    art_ascii()
    ideal_molecular()
    cal_p()

    volume = ((grams / molecular_mass)* r * temperature) / pressure

    print(f"P = {pressure} atm\ng/Mw = {grams}/{molecular_mass} \nR = {r}\nT = {temperature} K\n\nV = {volume:.2f} L")