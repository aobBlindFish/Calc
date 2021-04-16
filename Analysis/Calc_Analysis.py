# Import
import os, sys, inspect

# imports from parent folder
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)
import math
import BasicMath
import StringPreset

# Import
# Newtons Method for roots


class FuncX:  # ax^(b)
    def __init__(self, a, b):
        self.a = BasicMath.constant_round(a, 9)
        self.b = BasicMath.constant_round(b, 9)
        if self.a == 0:
            is_zero = True
        else:
            is_zero = False
        self.is_zero = is_zero

    def x_to_y(self, x):
        try:
            y = self.a * pow(x, self.b)
        except ValueError:
            sys.exit("Stelle nicht im Definitionsbereich")
        return y

    def display(self):
        # adjust a
        if self.a == 1:
            a_str = ""
        elif self.a == -1:
            a_str = "-"
        else:
            a_str = str(self.a)
        # adjust b
        if self.b == 1:
            b_str = ""
        else:
            b_str = "^(" + str(self.b) + ")"
        # adjust all
        if self.b == 0:
            fx_str = str(self.a)
        else:
            fx_str = a_str + "x" + b_str
        return fx_str

    def derivative(self):
        drv_a = self.a * self.b
        drv_b = self.b - 1
        if self.b == 0:
            drv_a = 0
            drv_b = 0
        return FuncX(drv_a, drv_b)


class Expo:  # e^f(x)
    def __init__(self, a, ex):
        self.a = a
        self.ex = ex
        if self.a == 0:
            is_zero = True
        else:
            is_zero = False
        self.is_zero = is_zero

    def x_to_y(self, x):
        try:
            y = self.a * pow(math.e, self.ex.x_to_y(x))
        except ValueError:
            sys.exit("Stelle nicht im Definitionsbereich")
        return y

    def display(self):
        # adjust a
        if self.a == 1:
            a_str = ""
        elif self.a == -1:
            a_str = "-"
        else:
            a_str = str(self.a)
        # adjust ex
        ex_str = "^(" + self.ex.display() + ")"
        # adjust all
        if self.ex.is_zero:
            fx_str = str(self.a)
        else:
            fx_str = a_str + "e" + ex_str
        return fx_str

    def derivative(self):  # chain rule
        if self.is_zero:
            return Expo(0, FuncX(0, 0))
        else:
            return Product([self, self.ex.derivative()])


class Sum:
    def __init__(self, sum_list):
        if len(sum_list) < 2:
            sys.exit("Keine Summe vorhanden")
        self.sum_list = sum_list
        is_zero = True
        for i in self.sum_list:
            if not i.is_zero:
                is_zero = False
        self.is_zero = is_zero

    def x_to_y(self, x):
        y = 0
        for i in self.sum_list:
            y += i.x_to_y(x)
        return y

    def display(self):
        sum_str = ""
        for i in self.sum_list:
            if not i.is_zero:
                if i.a > 0:
                    sum_str += " + "
                    sum_str += i.display()
                else:
                    sum_str += " - "
                    sum_str += StringPreset.str_trim(i.display(), 1)
        if sum_str[:3] == " + ":
            sum_str = StringPreset.str_trim(sum_str, 3)
        elif sum_str[:3] == " - ":
            sum_str = StringPreset.str_trim(sum_str, 1)
        return sum_str

    def derivative(self):
        derivative_list = []
        for i in self.sum_list:
            derivative_list.append(i.derivative())
        return Sum(derivative_list)


class Product:
    def __init__(self, product_list):
        if len(product_list) < 2:
            sys.exit("Kein Produkt vorhanden")
        self.product_list = product_list
        is_zero = False
        for i in self.product_list:
            if i.is_zero:
                is_zero = True
        self.is_zero = is_zero

    def x_to_y(self, x):
        y = 1
        for i in self.product_list:
            y = y * i.x_to_y(x)
        return y

    def display(self):
        sum_str = ""
        return sum_str

    def derivative(self):
        if len(self.product_list) != 2:
            pair_list = []
            if len(self.product_list) % 2 == 0:
                leftover = FuncX(1, 0)
                for i in range(0, len(self.product_list), 2):
                    pair_list.append([self.product_list[i], self.product_list[i + 1]])
            else:
                leftover = self.product_list[0]
                for i in range(1, len(self.product_list), 2):
                    pair_list.append([self.product_list[i], self.product_list[i + 1]])
        else:
            return Sum(
                [
                    Product([self.product_list[0], self.product_list[1].derivative()]),
                    Product([self.product_list[1], self.product_list[0].derivative()]),
                ]
            )


def sum_sort(function):
    func_x_list = []
    if type(function) == Sum:
        # FuncX
        input_list = []
        sum_sort_list = []
        for i in function.sum_list:
            if type(i) == FuncX:
                input_list.append([i.a, i.b])
        sorted_list = sorted(
            input_list, key=lambda list_item: list_item[1], reverse=True
        )
        for i in sorted_list:
            item_a = i[0]
            item_b = i[1]
            for j in sorted_list:
                if j[1] == i[1]:
                    item_a += j[0]
            if [item_a - i[0], item_b] not in sum_sort_list:
                sum_sort_list.append([item_a - i[0], item_b])
        for i in sum_sort_list:
            func_x_list.append(FuncX(i[0], i[1]))
    else:
        return function
    return Sum(func_x_list)


bb = Expo(-0.9, Sum([FuncX(1, 2), FuncX(-1, 1)]))
aa = Sum(
    [
        FuncX(0.25, 3),
        FuncX(-3, 2),
        FuncX(9, 1),
        FuncX(2, 2),
        FuncX(-4, 1),
        FuncX(6, 0),
        bb,
    ]
)
cc = Product([FuncX(1, 1), Expo(1, FuncX(1, 1))])
print(cc.display())
