from utils.logger import *
from utils.center import *

r = 0.0821

def mw_p():
    
    volume = volume_cal("PV = g/MwRT")
    grams = grams_cal("PV = g/MwRT")
    molecular_weight = molecular_weight_cal("PV = g/MwRT")
    temperature = temperature_cal("PV = g/MwRT")

    pressure = ((grams / molecular_weight)* r * temperature) / volume

    print(f"V = {volume} L\ng/Mw = {grams}/{molecular_weight} g/mol\nR = {r}\nT = {temperature} K\n\nP = {pressure:.2f} atm")

def mw_v():
    
    pressure = pressure_cal("PV = g/MwRT")
    grams = grams_cal("PV = g/MwRT")
    molecular_weight = molecular_weight_cal("PV = g/MwRT")
    temperature = temperature_cal("PV = g/MwRT")

    volume = ((grams / molecular_weight) * r * temperature) / pressure

    print(f"P = {pressure} atm\ng/Mw = {grams}/{molecular_weight} g/mol\nR = {r}\nT = {temperature} K\n\nV = {volume:.2f} L")

def mw_mw():
    
    pressure = pressure_cal("PV = g/MwRT")
    volume = volume_cal("PV = g/MwRT")
    temperature = temperature_cal("PV = g/MwRT")

    grams_of_molecular_weight = (pressure * volume) / (r * temperature)

    print(f"P = {pressure} atm\nV = {volume:.2f} L \nR = {r}\nT = {temperature} K\n\ng/Mw = {grams_of_molecular_weight:.4f} g/mol")

def mw_t():
    
    pressure = pressure_cal("PV = g/MwRT")
    volume = volume_cal("PV = g/MwRT")
    grams = grams_cal("PV = g/MwRT")
    molecular_weight = molecular_weight_cal("PV = g/MwRT")

    temperature = (pressure * volume) / ((grams / molecular_weight) * r)
    temperature_C = temperature - 273

    print(f"P = {pressure} atm\nV = {volume:.2f} L \nR = {r}\ng/Mw = {grams}/{molecular_weight} g/mol\n\nT = {temperature:.2f} K\nT = {temperature_C:.2f} C")
