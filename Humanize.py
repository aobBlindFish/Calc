import sys

pronoun_m = ["Er", "Sein", "Ihm"]
pronoun_w = ["Sie", "Ihr", "Ihr"]
pronoun_list = [pronoun_m, pronoun_w]


def pronoun(sex, pronoun_nmb):  # m == 0; w == 1
    return pronoun_list[sex][pronoun_nmb]
