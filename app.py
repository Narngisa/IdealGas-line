from utils.logger import *
from utils.std_gas import *
from utils.mw_gas import *
from utils.dst_gas import *

def home():

    choice = choice_func()
    
    if choice == 0:
        calculate = calculate_std()

        if calculate == 0:
            std_p()
        elif calculate == 1:
            std_v()
        elif calculate == 2:
            std_n()
        elif calculate == 3:
            std_t()
    
    elif choice == 1:
        calculate = calculate_mw()

        if calculate == 0:
            mw_p()
        elif calculate == 1:
            mw_v()
        elif calculate == 2:
            mw_mw()
        elif calculate == 3:
            mw_t()

    elif choice == 2:
        calculate = calculate_d()

        if calculate == 0:
            dst_p()
        elif calculate == 1:
            dst_mw()
        elif calculate == 2:
            dst_d()
        elif calculate == 3:
            dst_t()

    print("\n")
    back_log()
