from math import *
import BasicMath
import sys


def bernoulli(n, k, p):
    # error messages
    n = int(BasicMath.constant_round(n, 0))
    k = int(BasicMath.constant_round(k, 0))
    if not BasicMath.custom_range(1, p, 0, -1):
        if not (p == 0 or p == 1):
            sys.exit("Bernoulli: p muss zwischen 0 und 1 sein")
    if not (n > k or n == k):
        sys.exit("Bernoulli: n < k")
    if n < 0 or k < 0:
        sys.exit("Bernoulli: n oder k negativ")
    # calculation
    return comb(n, k)*pow(p, k)*pow(1-p, n-k)


def lotto(uppercase, lowercase):
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
    return BasicMath.constant_round(output, 8)
