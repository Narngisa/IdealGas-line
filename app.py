from utils.logger import *
from utils.std_gas import *
from utils.mw_gas import *
from utils.dst_gas import *
from utils.mo_gas import *

def home():

    choice = choice_func()
   
    match choice:
        case 0:
            cal = calculate_std()
            std_p() if cal == 0 else std_v() if cal == 1 else std_n() if cal == 2 else std_t() if cal == 3 else None 
        case 1:
            cal = calculate_mv()
            mv_p() if cal == 0 else mv_v() if cal == 1 else mv_mw() if cal == 2 else mv_t() if cal == 3 else None 
        case 2:
            cal = calculate_d()
            dst_p() if cal == 0 else dst_mw() if dst == 1 else dst_d() if cal == 2 else dst_t() if cal == 3 else None 
        case 3:
            cal = calculate_mo()
            mo_p() if cal == 0 else mo_m() if dst == 1 else mo_t() if cal == 2 else None 
    
    print("\n")
    back_log()
