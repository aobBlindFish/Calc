from math import *


# Round
def constant_round(constant, rounder):
    if rounder > 9:
        rounder = 9
    return round(pow(10, floor(abs(rounder)))*constant)/pow(10, floor(abs(rounder)))
