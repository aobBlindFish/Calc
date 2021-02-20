from math import *


# Round
def constant_round(constant, rounder):
    if abs(rounder) > 9:
        rounder = 9
    else:
        rounder = abs(rounder)
    rounder = round(rounder)
    return round(pow(10, floor(abs(rounder)))*constant)/pow(10, floor(abs(rounder)))


# Range
def custom_range(top, constant, bottom, accuracy):
    output = False
    accuracy = constant_round(accuracy, 0)
    if accuracy == -1:
        accuracy = 9
    elif accuracy < 0:
        accuracy = abs(accuracy)
    top_round = constant_round(top, accuracy)
    bottom_round = constant_round(bottom, accuracy)
    c_round = constant_round(constant, accuracy)
    if top_round > c_round > bottom_round:
        output = True
    return output
