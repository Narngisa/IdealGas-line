from utils.logger import *
from utils.center import *

r = 0.0821

def std_p():
    
    volume = volume_cal("PV = nRT")
    mol = mol_cal("PV = nRT")
    temperature = temperature_cal("PV = nRT")


    pressure = (mol * r * temperature) / volume

    print(f"V = {volume} L\nn = {mol} mol\nR = {r}\nT = {temperature} K\n\nP = {pressure:.2f} atm")

def std_v():
    
    pressure = pressure_cal("PV = nRT")
    mol = mol_cal("PV = nRT")
    temperature = temperature_cal("PV = nRT")

    volume = (mol * r * temperature) / pressure

    print(f"P = {pressure} atm\nn = {mol} mol\nR = {r}\nT = {temperature} K\n\nV = {volume:.2f} L")

def std_n():
    
    pressure = pressure_cal("PV = nRT")
    volume = volume_cal("PV = nRT")
    temperature = temperature_cal("PV = nRT")

    mol = (pressure * volume) / (r * temperature)

    print(f"P = {pressure} atm\nV = {volume} L\nR = {r}\nT = {temperature} K\n\nn = {mol:.2f} mol")

def std_t():
    
    pressure = pressure_cal("PV = nRT")
    volume = volume_cal("PV = nRT")
    mol = mol_cal("PV = nRT")

    temperature = (pressure * volume) / (mol * r)
    temperature_C = temperature - 273

    print(f"P = {pressure} atm\nV = {volume} L\nR = {r}\nn = {mol} mol\n\nT = {temperature:.2f} K\nT = {temperature_C:.2f} C")
