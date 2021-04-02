import sys
import math
import random


def test_1(number):
    j = 1
    i = 1
    while i <= number:
        if c_mod(i, j):
            list = []
            for k in range(i):
                list.append(j / (k + 1))
            print()
            print(str(i) + ": " + str(j))
            print(list)
            print()
            i += 1
        j += 1


def c_mod(a, b):
    list = []
    for i in range(a):
        list.append(i + 1)
    if a > b:
        return False
    else:
        output = True
        for i in list:
            if b % i != 0:
                output = False
        return output


def if_prime(a):
    output = True
    if a == 1:
        return False
    list = []
    for i in range(a - 2):
        list.append(i + 2)
    for i in list:
        if a % i == 0:
            return False
    return output


def amount_prime(amount, typ=1):
    counter = 1
    suspect = 1
    list = []
    while counter <= amount:
        if if_prime(suspect):
            counter += 1
            list.append(suspect)
        suspect += 1
    if typ == 1:
        return list
    elif typ == 2:
        return list[amount - 1]


class Point:
    def __init__(self, x, y):
        if x * x + y * y > 1:
            sys.exit("not in circle")
        self.x = x
        self.y = y


pair_list = []
dis_list = []


def make_pair():
    pair = []
    i = 0
    while i < 2:
        try:
            a = Point(random.uniform(-1, 1), random.uniform(-1, 1))
            pair.append(a)
            i += 1
        except SystemExit:
            i = i
    pair_list.append(pair)
    dis_list.append(dis(pair[0], pair[1]))
    return pair


def dis(a, b):
    return math.sqrt((b.x - a.x) * (b.x - a.x) + (b.y - a.y) * (b.y - a.y))


def average(num_list):
    output = 0
    for i in num_list:
        output += i
    output = output / len(num_list)
    return output


# for i in range(1000000):
#     make_pair()
# Average disance between points in a unit circle: 128 / (45 * math.pi)
# print(average(dis_list) - 128 / (45 * math.pi))
