from utils.logger import *
from utils.center import *

r = 0.0821

def dst_p():

    molecular_weight = molecular_weight_cal("PMw = DRT")
    density = density_cal("PMw = DRT")
    temperature = temperature_cal("PMw = DRT")

    pressure = (density * r * temperature) / molecular_weight
    print(f"D = {density} g/L\nMw = {molecular_weight} mol\nR = {r}\nT = {temperature} K\n\nP = {pressure:.2f} atm")

def dst_mw():

    pressure = pressure_cal("PMw = DRT")
    density = density_cal("PMw = DRT")
    temperature = temperature_cal("PMw = DRT")

    molecular_weight = (density * r * temperature) / pressure
    print(f"D = {density} g/L\nP = {pressure:.2f} atm\nR = {r}\nT = {temperature} K\n\nMw = {molecular_weight:.2f} mol")

def dst_d():

    pressure = pressure_cal("PMw = DRT")
    molecular_weight = molecular_weight_cal("PMw = DRT")
    temperature = temperature_cal("PMw = DRT")

    density = (pressure * molecular_weight) / (r * temperature)
    print(f"P = {pressure:.2f} atm\nMw = {molecular_weight} mol\nR = {r}\nT = {temperature} K\n\nD = {density:.2f} g/L")

def dst_t():

    pressure = pressure_cal("PMw = DRT")
    molecular_weight = molecular_weight_cal("PMw = DRT")
    density = density_cal("PMw = DRT")

    temperature = (pressure * molecular_weight) / (r * density)
    temperature_C = temperature - 273
    print(f"P = {pressure:.2f} atm\nMw = {molecular_weight} mol\nR = {r}\nD = {density} g/L\n\nT = {temperature:.2f} K\nT = {temperature_C:.1f} C")

