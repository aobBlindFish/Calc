from math import *
import sys
import BasicMath as Bm


class Bernoulli:  # kumulierte P(X) fehlen
    def __init__(self, n, k, p, rounder=2):
        # error messages
        n = int(Bm.constant_round(n, 0))
        k = int(Bm.constant_round(k, 0))
        if not Bm.custom_range(1, p, 0, -1):
            if not (p == 0 or p == 1):
                sys.exit("Bernoulli: p muss zwischen 0 und 1 sein")
        if not (n > k or n == k):
            sys.exit("Bernoulli: n < k")
        if n < 0 or k < 0:
            sys.exit("Bernoulli: n oder k negativ")
        # assign
        self.n = n
        self.k = k
        self.p = p
        self.rounder = rounder

    def prob(self):
        return Bm.constant_round(comb(self.n, self.k)*pow(self.p, self.k)*pow(1-self.p, self.n-self.k), self.rounder)
    
    def exp_value(self):
        return Bm.constant_round(self.n * self.k, self.rounder)

    def standard_dev(self):
        return Bm.constant_round(sqrt(self.n * self.p * (1-self.p)), self.rounder)


class Discreet:
    def __init__(self, uppercase, lowercase):
        if len(uppercase) != len(lowercase):
            sys.exit("Listen sind ungleich lang")


def lotto(uppercase, lowercase, rounder=2):
    # error messages
    if len(uppercase) != len(lowercase):
        sys.exit("Lotto: Listen sind ungleich lang")
    for category in uppercase:
        category_nmb = uppercase.index(category)
        if uppercase[category_nmb] < lowercase[category_nmb]:
            sys.exit("Lotto: A < a")
    # calculation
    main_n = 0
    sub_n = 0
    for category in uppercase:
        main_n += category
    for category in lowercase:
        sub_n += category
    output = 1/comb(main_n, sub_n)
    for category in uppercase:
        category_nmb = uppercase.index(category)
        output = output*comb(uppercase[category_nmb], lowercase[category_nmb])
    return Bm.constant_round(output, rounder)
