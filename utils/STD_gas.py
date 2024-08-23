from utils.logger import *

r = 0.0821

def equation_p():

    clear_log()
    art_ascii()
    ideal_standard()
    volume = float(input("V: "))

    clear_log()
    art_ascii()
    ideal_standard()
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
    ideal_standard()
    mol = float(input("n: "))

    clear_log()
    art_ascii()
    ideal_standard()
    temperature = float(input("T: "))

    clear_log()
    art_ascii()
    ideal_standard()
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
    ideal_standard()
    cal_p()

    pressure = (mol * r * temperature) / volume

    print(f"V = {volume} L\nn = {mol} mol\nR = {r}\nT = {temperature} K\n\nP = {pressure:.2f} atm")

def equation_v():

    clear_log()
    art_ascii()
    ideal_standard()
    pressure = float(input("P: "))

    clear_log()
    art_ascii()
    ideal_standard()
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
    ideal_standard()
    mol = float(input("n: "))

    clear_log()
    art_ascii()
    ideal_standard()
    temperature = float(input("T: "))

    clear_log()
    art_ascii()
    ideal_standard()
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
    ideal_standard()
    cal_v()

    volume = (mol * r * temperature) / pressure

    print(f"P = {pressure} atm\nn = {mol} mol\nR = {r}\nT = {temperature} K\n\nV = {volume:.2f} L")

def equation_n():
    
    clear_log()
    art_ascii()
    ideal_standard()
    pressure = float(input("P: "))

    clear_log()
    art_ascii()
    ideal_standard()
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
    ideal_standard()
    volume = float(input("V: "))

    clear_log()
    art_ascii()
    ideal_standard()
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
    ideal_standard()
    temperature = float(input("T: "))

    clear_log()
    art_ascii()
    ideal_standard()
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
    ideal_standard()
    cal_n()

    mol = (pressure * volume) / (r * temperature)

    print(f"P = {pressure} atm\nV = {volume} L\nR = {r}\nT = {temperature} K\n\nn = {mol:.2f} mol")

def equation_t():

    clear_log()
    art_ascii()
    ideal_standard()
    pressure = float(input("P: "))

    clear_log()
    art_ascii()
    ideal_standard()
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
    ideal_standard()
    volume = float(input("V: "))

    clear_log()
    art_ascii()
    ideal_standard()
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
    ideal_standard()
    mol = float(input("n: "))

    clear_log()
    art_ascii()
    ideal_standard()
    cal_t()

    temperature = (pressure * volume) / (mol * r)
    C_temperature = temperature - 273

    print(f"P = {pressure} atm\nV = {volume} L\nR = {r}\nn = {temperature} mol\n\nT = {temperature:.2f} K\nT = {C_temperature:.2f} C")