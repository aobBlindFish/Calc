# pronoun_m = [Nominativ, Genitiv, Dativ, Akkusativ, ...]
pronoun_m = ["Er", "Seiner", "Ihm", "Ihn", "Der"]
pronoun_w = ["Sie", "Ihrer", "Ihr", "Sie", "Die"]
pronoun_list = [pronoun_m, pronoun_w]


class Identity:
    def __init__(self, name, sex):
        self.name = str(name)
        self.sex = sex

    def pronoun(self, pronoun_nmb):  # m == 0; w == 1
        return pronoun_list[self.sex][pronoun_nmb]
