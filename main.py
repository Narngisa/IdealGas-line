from utils.logger import *
from app import *

def tool():

    while True:
        home() if home_log() == True else exit()

if __name__ == "__main__":
    tool()
