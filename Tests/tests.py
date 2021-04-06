# Import
import os, sys, inspect

# imports from parent folder
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)
import math
import random
import BasicMath

# after input x: returns lowest number y for y%x == 0 and y%(x-1) == 0 and y%(x-2) == 0 ...
def test_1(number):
    def c_mod(a, b):  # checks if b%a == 0 for a and all N below a
        list = []
        if a > b:
            return False
        else:
            for i in range(a):
                list.append(i + 1)
            output = True
            for i in list:
                if b % i != 0:
                    output = False
            return output

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


# returns the nth prime
def amount_prime(amount, typ=1):
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


# Average disance between points in a unit circle
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


for i in range(1):
    make_pair()
# Average disance between points in a unit circle: 128 / (45 * math.pi)
# print(average(dis_list) - 128 / (45 * math.pi))


# Custom roots of natural numbers without sqrt()
def custom_root(num, degree=2, rnd=6):
    def iterate_root(num, degree=2, start=20):
        return (1 / degree) * ((degree - 1) * start + (num / (start ** (degree - 1))))

    a = iterate_root(num, degree)
    b = iterate_root(num, degree, a)
    while not BasicMath.custom_comp(a, b, rnd):
        a = b
        b = iterate_root(num, degree, b)
    return BasicMath.constant_round(b, rnd)


# golden ratio
def golden_ratio(num=5, rnd=6):
    def golden_ratio_iterate(num):
        return 1 + (1 / num)

    a = num
    b = golden_ratio_iterate(num)
    while not BasicMath.custom_comp(a, b, rnd):
        a = b
        b = golden_ratio_iterate(b)
    return BasicMath.constant_round(b, rnd)
