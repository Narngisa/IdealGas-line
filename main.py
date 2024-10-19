from utils.logger import *
from app import *

def tool():
    selected_function = home_log()

    if selected_function == "home":
        home()

if __name__ == "__main__":
    tool()