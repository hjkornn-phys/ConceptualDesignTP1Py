import os
import sys

if 'darwin' in sys.platform:
    SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
    sys.path.append(os.path.dirname(SCRIPT_DIR))

import math
import string
import packages.AVLFunctions as AVLF
import packages.AVLAircraft as Acft
import packages.MainFunctions as MainF



# Specs = open("Specs1.csv","a")
# Specs.write("C, R, S, V")
# Specs.close()

s = [1,1,1]
v = [2,2,2]
L = s+v

print(L)

