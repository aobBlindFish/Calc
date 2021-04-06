from math import *


# Round
def constant_round(constant, rounder=2):
    if abs(rounder) > 19:
        rounder = 19
    else:
        rounder = abs(rounder)
    rounder = round(rounder)
    return round(pow(10, floor(abs(rounder))) * constant) / pow(10, floor(abs(rounder)))


# Comparison
def custom_comp(num_1, num_2, rnd=8):
    a = constant_round(num_1, rnd)
    b = constant_round(num_2, rnd)
    return a == b


# Range
def custom_range(top, constant, bottom, accuracy=2):
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


# Prime
def if_prime(a):
    try:
        a = int(a)
        if a <= 1:
            return False
        list = []
        for i in range(a - 2):
            list.append(i + 2)
        for i in list:
            if a % i == 0:
                return False
        return True
    except ValueError:
        return False
