from utils.logger import *
from utils.STD_gas import *

def app():
    clear_log()
    art_ascii()
    print("Choose a function to calculate.\n[0] PV = nRT\n[1] PV = g/MwRT\n[2] PM = DRT")

    try:
        result = int(input("\n>> "))
        if result == 0:
            clear_log()
            art_ascii()
            ideal_standard()
            print("What do you want to calculate?")
            print("[0] P\n[1] V\n[2] N\n[3] T\n")

            value = int(input("\n>> "))

            if value == 0:
                equation_p()

            elif value == 1:
                equation_v()
            elif value == 2:
                equation_n()
            elif value == 3:
                equation_t()

            else:
                error_log("Error: No value in function !!")
                back_log()

            return_log()
            
        elif result == 1 or result == 2:
            error_log("Error: Comimg soon !!")
            back_log()

        else:
            error_log("Error: No function !!")
            back_log()
    except:
        error_log("Value not type int !!")
        back_log()