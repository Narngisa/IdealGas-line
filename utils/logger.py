import os
import webbrowser as wb
import subprocess
import sys

ascii = """
\033[31m  _____    _            _    _____             _                    
\033[33m |_   _|  | |          | |  / ____|           | |                   
\033[32m   | |  __| | ___  __ _| | | |  __  __ _ ___  | |     __ ___      __
\033[36m   | | / _` |/ _ \/ _` | | | | |_ |/ _` / __| | |    / _` \ \ /\ / /
\033[34m  _| || (_| |  __/ (_| | | | |__| | (_| \__ \ | |___| (_| |\ V  V / 
\033[35m |_____\__,_|\___|\__,_|_|  \_____|\__,_|___/ |______\__,_| \_/\_/     \033[37m                                                                                                                                                                                                                                                                                                   
"""

def art_ascii():
    print(ascii)

def error_log(log_message: str) -> None:
    os.system("cls" if os.name == "nt" else "clear")
    print(f'\033[91m{log_message}')

def back_log():
    print(f"[y] Return")
    print(f"[e] Exit to app")
    er = str(input(">> ").lower())

    if er == "y":
        subprocess.run([sys.executable, "main.py"])

    elif er == "e":
        exit()
    else:
        wb.open("https://youtu.be/xvFZjo5PgG0?si=6i6PR1wnUKkszPV7")

def clear_log():
    os.system("cls" if os.name == "nt" else "clear")

def ideal_standard():
    print("Function: PV = nRT")

def ideal_molecular():
    print("Function: PV = g/MwRT")

def return_log():
    print(f"\n[y] Return")
    rl = str(input(">> ").lower())

    if rl == "y":
        subprocess.run([sys.executable, "main.py"])
    else:
        wb.open("https://youtu.be/xvFZjo5PgG0?si=6i6PR1wnUKkszPV7")

def cal_p():
    print("Calculate: Pressure")

def cal_v():
    print("Calculate: Volume")

def cal_n():
    print("Calculate: mol")

def cal_g():
    print("Calculate: grams")

def cal_mw():
    print("Calculate: molecular mass")

def cal_t():
    print("Calculate: Temperature")
