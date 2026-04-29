from utils.logger import *
from utils.center import *

r = 0.0821

def mo_p():
    molar = molar_cal("P = MRT")
    temperature = temperature_cal("P = MRT")

    pressure = molar * r * temperature
    print(f"M = {molar} mol/L\nR = {r}\nT = {temperature} K\n\nP = {pressure:.2f} atm")

def mo_m():
    pressure = pressure_cal("P = MRT")
    temperature = temperature_cal("P = MRT")

    molar = pressure / (r * temperature)
    print(f"P = {pressure:.2f} atm\nR = {r}\nT = {temperature} K\n\nM = {molar:.4f} mol/L")

def mo_t():
    pressure = pressure_cal("P = MRT")
    molar = molar_cal("P = MRT")

    temperature = pressure / (molar * r)
    temperature_C = temperature - 273
    print(f"P = {pressure:.2f} atm\nM = {molar} mol/L\nR = {r}\n\nT = {temperature:.2f} K\nT = {temperature_C:.2f} C")
