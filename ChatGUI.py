import sys
import Calc
import random

'''
Todo:
- Proper Machine Name
'''
'''
Stages:
0 == Introduction - Topic chosen
1 == Objects asked - Objects chosen - task list_filled
2 == for object in task_list: Chosen objects defined as Calc.py-objects
3 == for object in task_list: Solution calculated
4 == for object in task_list: Calc.py-solution defined into words
5 == for object in task_list: Solution returned
6 == Repeat or End
'''
# Meta Var
program_name = "Siri"

# Choice Arrays
task_list = []

user_true = ["JA", "KLAR", "JUP", "JAP", "GENAU", "RICHTIG", "KORREKT"]
user_false = ["NEIN", "NE", "NICHT", "FALSCH", "UNGENAU"]
user_boolean = [user_true, user_false]

topic_dis = ["Abstand", "ABSTAND", "ABSTÄNDE", "DISTANZ", "DISTANZEN", "ENTFERNUNG", "ENTFERNUNGEN"]
topic_cross = ["Schnittmenge", "SCHNITTPUNKT", "SCHNITTPUNKTE", "SCHNITTGERADE", "SCHNITTGERADEN", "SCHNITTMENGE",
               "SCHNITTMENGEN"]
topic_contain = ["Lagebeziehung", "LAGEBEZIEHUNG", "LAGEBEZIEHUNGEN", "LAGEVERHÄLTNIS", "LAGE"]
topic = [topic_dis, topic_cross, topic_contain]

object_point = ["Punkt", "PUNKT"]
object_line = ["Gerade", "GERADE", "LINIE"]
object_plane = ["Ebene", "EBENE", "FLÄCHE", "OBERFLÄCHE"]
object_vector = ["Vektor", "VEKTOR", "RICHTUNG"]
object_full_list = [object_point, object_line, object_plane, object_vector]

object_type_pt_pt = ["PUNKT", "PUNKTE"]
object_type_pt = [object_type_pt_pt]
object_type_vc_vc = ["VEKTOR", "VEKTOREN"]
object_type_vc = [object_type_vc_vc]
object_type_ln_pt = ["PUNKT", "PUNKTE"]
object_type_ln_par = ["PARAMETER", "PARAMETERFORM", "VEKTOR", "VEKTOREN", "RICHTUNGSVEKTOR"]
object_type_ln = [object_type_ln_par, object_type_ln_pt]
object_type_pl_par = ["PARAMETER", "PARAMETERFORM", "VEKTOR", "VEKTOREN", "RICHTUNGSVEKTOR", "RICHTUNGSVEKTOREN",
                      "SPANNVEKTOR", "SPANNVEKTOREN"]
object_type_pl_norm = ["NORMAL", "NORMALE", "NORMALENFORM"]
object_type_pl_coord = ["KOORDINATE", "KOORDINATEN", "KOORDINATENFORM"]
object_type_pl_pt = ["PUNKT", "PUNKTE", "GRUPPE VON MEHREREN PUNKTEN", "MEHRERE PUNKTE", "."]
object_type_pl = [object_type_pl_par, object_type_pl_norm, object_type_pl_coord, object_type_pl_pt]
object_type_full_list = [object_type_pt, object_type_ln, object_type_pl, object_type_vc]


# Task 2


def stage_2_pl_pt(pl_aa, pl_bb, pl_cc):
    output = Calc.Plane(Calc.Conv.Pl.Pt.par(pl_aa, pl_bb, pl_cc)[0], Calc.Conv.Pl.Pt.par(pl_aa, pl_bb, pl_cc)[1],
                        Calc.Conv.Pl.Pt.par(pl_aa, pl_bb, pl_cc)[2])
    return output


def stage_2_pl_coord(a, b, c, d):
    output = Calc.Plane(Calc.Conv.Pl.Coord.par(a, b, c, d)[0], Calc.Conv.Pl.Coord.par(a, b, c, d)[1],
                        Calc.Conv.Pl.Coord.par(a, b, c, d)[2])
    return output


def stage_2_pl_norm(sp, normal):
    output = Calc.Plane(Calc.Conv.Pl.Norm.par(sp, normal)[0], Calc.Conv.Pl.Norm.par(sp, normal)[1],
                        Calc.Conv.Pl.Norm.par(sp, normal)[2])
    return output


def stage_2_pl_par(sp, dr1, dr2):
    output = Calc.Plane(sp, dr1, dr2)
    return output


def stage_2_ln_pt(ln_pt_aa, ln_pt_bb):
    output = Calc.Line(Calc.Conv.Ln.Pt.par(ln_pt_aa, ln_pt_bb)[0], Calc.Conv.Ln.Pt.par(ln_pt_aa, ln_pt_bb)[1])
    return output


def stage_2_ln_par(sp, dr):
    output = Calc.Line(sp, dr)
    return output


def stage_2_vc(x, y, z):
    output = Calc.Vector(x, y, z)
    return output


def stage_2_pt(x, y, z):
    output = Calc.Point(x, y, z)
    return output


def stage_2_plane():
    pl_understand = False
    print("In welcher Form kennst du diese Ebene?")
    pl_type = 0
    while not pl_understand:
        user_pl_type = input().upper()
        for ii in object_type_pl:
            for jj in ii:
                if user_pl_type == jj:
                    pl_understand = True
                    pl_type = object_type_pl.index(ii)
        if not pl_understand:
            print(misunderstand[random.randint(0, len(misunderstand) - 1)] +
                  "\nIn welcher Form kennst du diese Ebene? In der Parameterform, "
                  "Normalenform, Koordinatenform oder als Gruppe von mehreren Punkten?")
    return pl_type


# Task Object & Stage 2
class Task:
    def __init__(self, task_name, chosen_topic, obj_type1, obj_type2):
        self.task_name = task_name
        self.complete = False
        self.chosen_topic = chosen_topic
        self.obj_types = [obj_type1, obj_type2]
        self.obj_calc = []

    def obj_define(self):
        print("\nOkay, zu " + self.task_name + "(" + topic[self.chosen_topic][0] + " zwischen " +
              object_full_list[self.obj_types[0]][0] + " und " + object_full_list[self.obj_types[1]][0] + "):")
        name_i = 1
        while name_i <= len(self.obj_types):
            print("Das " + str(name_i) + ". Objekt..")
            if self.obj_types[0] == 2:
                obj_pl_type = stage_2_plane()
                if obj_pl_type == 0:
                    print("Okay gut.")
                    pl_par_sp_x = 0
                    pl_par_sp_y = 0
                    pl_par_sp_z = 0
                    pl_par_dr1_x = 0
                    pl_par_dr1_y = 0
                    pl_par_dr1_z = 0
                    pl_par_dr2_x = 0
                    pl_par_dr2_y = 0
                    pl_par_dr2_z = 0
                    pl_par_correct = False
                    while not pl_par_correct:
                        # Support
                        pl_par_sp_confirm = False
                        pl_par_sp_confirm_no = False
                        while not pl_par_sp_confirm:
                            pl_par_sp_x_understand = False
                            while not pl_par_sp_x_understand:
                                try:
                                    pl_par_sp_x = float(input("Wie lautet dein Stützvektor(x-Koordinate): "))
                                    pl_par_sp_x_understand = True
                                except ValueError:
                                    print(misunderstand[random.randint(0, len(misunderstand) - 1)])
                            pl_par_sp_y_understand = False
                            while not pl_par_sp_y_understand:
                                try:
                                    pl_par_sp_y = float(input("Wie lautet dein Stützvektor(y-Koordinate): "))
                                    pl_par_sp_y_understand = True
                                except ValueError:
                                    print(misunderstand[random.randint(0, len(misunderstand) - 1)])
                            pl_par_sp_z_understand = False
                            while not pl_par_sp_z_understand:
                                try:
                                    pl_par_sp_z = float(input("Wie lautet dein Stützvektor(z-Koordinate): "))
                                    pl_par_sp_z_understand = True
                                except ValueError:
                                    print(misunderstand[random.randint(0, len(misunderstand) - 1)])
                            # sp_confirm
                            print("Also Stützvektor s = (" + str(pl_par_sp_x) + "|" + str(pl_par_sp_y) + "|" +
                                  str(pl_par_sp_z) + ")?")
                            while not pl_par_sp_confirm:
                                user_pl_sp_confirm = input().upper()
                                for ii in user_boolean:
                                    for jj in ii:
                                        if user_pl_sp_confirm == jj:
                                            if user_boolean.index(ii) == 0:
                                                pl_par_sp_confirm = True
                                                print("Gut.")
                                            elif user_boolean.index(ii) == 1:
                                                pl_par_sp_confirm_no = True
                                                print("Okay, versuchen wir das nochmal.")
                                if not (pl_par_sp_confirm_no or pl_par_sp_confirm):
                                    print(misunderstand[random.randint(0, len(misunderstand) - 1)])
                                if pl_par_sp_confirm_no:
                                    break
                        # Direction 1
                        pl_par_dr1_confirm = False
                        pl_par_dr1_confirm_no = False
                        while not pl_par_dr1_confirm:
                            pl_par_dr1_x_understand = False
                            while not pl_par_dr1_x_understand:
                                try:
                                    pl_par_dr1_x = float(input("Wie lautet dein erster "
                                                               "Richtungsvektor(x-Koordinate): "))
                                    pl_par_dr1_x_understand = True
                                except ValueError:
                                    print(misunderstand[random.randint(0, len(misunderstand) - 1)])
                            pl_par_dr1_y_understand = False
                            while not pl_par_dr1_y_understand:
                                try:
                                    pl_par_dr1_y = float(input("Wie lautet dein erster "
                                                               "Richtungsvektor(y-Koordinate): "))
                                    pl_par_dr1_y_understand = True
                                except ValueError:
                                    print(misunderstand[random.randint(0, len(misunderstand) - 1)])
                            pl_par_dr1_z_understand = False
                            while not pl_par_dr1_z_understand:
                                try:
                                    pl_par_dr1_z = float(input("Wie lautet dein erster "
                                                               "Richtungsvektor(z-Koordinate): "))
                                    pl_par_dr1_z_understand = True
                                except ValueError:
                                    print(misunderstand[random.randint(0, len(misunderstand) - 1)])
                            # dr1_confirm
                            print("Also Spannvektor d1 = (" + str(pl_par_dr1_x) + "|" + str(pl_par_dr1_y) + "|" +
                                  str(pl_par_dr1_z) + ")?")
                            while not pl_par_dr1_confirm:
                                user_pl_dr1_confirm = input().upper()
                                for ii in user_boolean:
                                    for jj in ii:
                                        if user_pl_dr1_confirm == jj:
                                            if user_boolean.index(ii) == 0:
                                                pl_par_dr1_confirm = True
                                                print("Gut.")
                                            elif user_boolean.index(ii) == 1:
                                                pl_par_dr1_confirm_no = True
                                                print("Okay, versuchen wir das nochmal.")
                                if not (pl_par_dr1_confirm_no or pl_par_dr1_confirm):
                                    print(misunderstand[random.randint(0, len(misunderstand) - 1)])
                                if pl_par_dr1_confirm_no:
                                    break

                        # Direction 2
                        pl_par_dr2_confirm = False
                        pl_par_dr2_confirm_no = False
                        while not pl_par_dr2_confirm:
                            pl_par_dr2_x_understand = False
                            while not pl_par_dr2_x_understand:
                                try:
                                    pl_par_dr2_x = float(input("Wie lautet dein zweiter "
                                                               "Richtungsvektor(x-Koordinate): "))
                                    pl_par_dr2_x_understand = True
                                except ValueError:
                                    print(misunderstand[random.randint(0, len(misunderstand) - 1)])
                            pl_par_dr2_y_understand = False
                            while not pl_par_dr2_y_understand:
                                try:
                                    pl_par_dr2_y = float(input("Wie lautet dein zweiter "
                                                               "Richtungsvektor(y-Koordinate): "))
                                    pl_par_dr2_y_understand = True
                                except ValueError:
                                    print(misunderstand[random.randint(0, len(misunderstand) - 1)])
                            pl_par_dr2_z_understand = False
                            while not pl_par_dr2_z_understand:
                                try:
                                    pl_par_dr2_z = float(input("Wie lautet dein zweiter "
                                                               "Richtungsvektor(z-Koordinate): "))
                                    pl_par_dr2_z_understand = True
                                except ValueError:
                                    print(misunderstand[random.randint(0, len(misunderstand) - 1)])
                            # dr2_confirm
                            print(
                                "Also Spannvektor d2 = (" + str(pl_par_dr2_x) + "|" + str(pl_par_dr2_y) + "|" +
                                str(pl_par_dr2_z) + ")?")
                            while not pl_par_dr2_confirm:
                                user_pl_dr2_confirm = input().upper()
                                for ii in user_boolean:
                                    for jj in ii:
                                        if user_pl_dr2_confirm == jj:
                                            if user_boolean.index(ii) == 0:
                                                pl_par_dr2_confirm = True
                                            elif user_boolean.index(ii) == 1:
                                                pl_par_dr2_confirm_no = True
                                                print("Okay, versuchen wir das nochmal.")
                                if not (pl_par_dr2_confirm_no or pl_par_dr2_confirm):
                                    print(misunderstand[random.randint(0, len(misunderstand) - 1)])
                                if pl_par_dr2_confirm_no:
                                    break
                        try:
                            object_1 = stage_2_pl_par(Calc.Vector(pl_par_sp_x, pl_par_sp_y, pl_par_sp_z),
                                                      Calc.Vector(pl_par_dr1_x, pl_par_dr1_y, pl_par_dr1_z),
                                                      Calc.Vector(pl_par_dr2_x, pl_par_dr2_y, pl_par_dr2_z))
                            self.obj_calc.append(object_1)
                            pl_par_correct = True
                            print("Perfekt.")
                        except SystemExit:
                            print("Diese Vektoren beschreiben keine eindeutige Ebene.\nVersuchen wir das nochmal.")
                elif obj_pl_type == 1:
                    print("Verstanden.")
                    pl_norm_sp_x = 0
                    pl_norm_sp_y = 0
                    pl_norm_sp_z = 0
                    pl_norm_norm_x = 0
                    pl_norm_norm_y = 0
                    pl_norm_norm_z = 0
                    # Support
                    pl_norm_sp_confirm = False
                    pl_norm_sp_confirm_no = False
                    while not pl_norm_sp_confirm:
                        pl_norm_sp_x_understand = False
                        while not pl_norm_sp_x_understand:
                            try:
                                pl_norm_sp_x = float(input("Wie lautet dein Stützvektor(x-Koordinate): "))
                                pl_norm_sp_x_understand = True
                            except ValueError:
                                print(misunderstand[random.randint(0, len(misunderstand) - 1)])
                        pl_norm_sp_y_understand = False
                        while not pl_norm_sp_y_understand:
                            try:
                                pl_norm_sp_y = float(input("Wie lautet dein Stützvektor(y-Koordinate): "))
                                pl_norm_sp_y_understand = True
                            except ValueError:
                                print(misunderstand[random.randint(0, len(misunderstand) - 1)])
                        pl_norm_sp_z_understand = False
                        while not pl_norm_sp_z_understand:
                            try:
                                pl_norm_sp_z = float(input("Wie lautet dein Stützvektor(z-Koordinate): "))
                                pl_norm_sp_z_understand = True
                            except ValueError:
                                print(misunderstand[random.randint(0, len(misunderstand) - 1)])
                        # sp_confirm
                        print("Also Stützvektor s = (" + str(pl_norm_sp_x) + "|" + str(pl_norm_sp_y) + "|" +
                              str(pl_norm_sp_z) + ")?")
                        while not pl_norm_sp_confirm:
                            user_pl_sp_confirm = input().upper()
                            for ii in user_boolean:
                                for jj in ii:
                                    if user_pl_sp_confirm == jj:
                                        if user_boolean.index(ii) == 0:
                                            pl_norm_sp_confirm = True
                                            print("Gut.")
                                        elif user_boolean.index(ii) == 1:
                                            pl_norm_sp_confirm_no = True
                                            print("Okay, versuchen wir das nochmal.")
                            if not (pl_norm_sp_confirm_no or pl_norm_sp_confirm):
                                print(misunderstand[random.randint(0, len(misunderstand) - 1)])
                            if pl_norm_sp_confirm_no:
                                break
                    # Normal
                    pl_norm_norm_correct = False
                    pl_norm_norm_confirm = False
                    pl_norm_norm_confirm_no = False
                    while not pl_norm_norm_confirm:
                        while (not pl_norm_norm_correct) or pl_norm_norm_confirm_no:
                            pl_norm_norm_confirm_no = False
                            pl_norm_norm_x_understand = False
                            while not pl_norm_norm_x_understand:
                                try:
                                    pl_norm_norm_x = float(input("Wie lautet dein Normalvektor(x-Koordinate): "))
                                    pl_norm_norm_x_understand = True
                                except ValueError:
                                    print(misunderstand[random.randint(0, len(misunderstand) - 1)])
                            pl_norm_norm_y_understand = False
                            while not pl_norm_norm_y_understand:
                                try:
                                    pl_norm_norm_y = float(input("Wie lautet dein Normalvektor(y-Koordinate): "))
                                    pl_norm_norm_y_understand = True
                                except ValueError:
                                    print(misunderstand[random.randint(0, len(misunderstand) - 1)])
                            pl_norm_norm_z_understand = False
                            while not pl_norm_norm_z_understand:
                                try:
                                    pl_norm_norm_z = float(input("Wie lautet dein Normalvektor(z-Koordinate): "))
                                    pl_norm_norm_z_understand = True
                                except ValueError:
                                    print(misunderstand[random.randint(0, len(misunderstand) - 1)])
                            if Calc.Vector(pl_norm_norm_x, pl_norm_norm_y, pl_norm_norm_z).fullzero:
                                print("Diese Normale hat eine Länge von 0 und deswegen keine Richtung."
                                      "\nVersuchen wir das nochmal.")
                                pl_norm_norm_correct = False
                            else:
                                pl_norm_norm_correct = True
                        # norm_confirm
                        print("Also Normalenvektor n = (" + str(pl_norm_norm_x) + "|" + str(pl_norm_norm_y) + "|" +
                              str(pl_norm_norm_z) + ")?")
                        while not pl_norm_norm_confirm:
                            user_pl_norm_confirm = input().upper()
                            for ii in user_boolean:
                                for jj in ii:
                                    if user_pl_norm_confirm == jj:
                                        if user_boolean.index(ii) == 0:
                                            pl_norm_norm_confirm = True
                                            pl_norm_norm_correct = True
                                            print("Verstanden.")
                                        elif user_boolean.index(ii) == 1:
                                            pl_norm_norm_confirm_no = True
                                            pl_norm_norm_correct = False
                                            print("Okay, versuchen wir das nochmal.")
                            if not (pl_norm_norm_confirm_no or pl_norm_norm_confirm):
                                print(misunderstand[random.randint(0, len(misunderstand) - 1)])
                            elif pl_norm_norm_confirm_no:
                                break

                    object_1 = stage_2_pl_norm(Calc.Vector(pl_norm_sp_x, pl_norm_sp_y, pl_norm_sp_z),
                                               Calc.Vector(pl_norm_norm_x, pl_norm_norm_y, pl_norm_norm_z))
                    self.obj_calc.append(object_1)
                elif obj_pl_type == 2:
                    print("Okay gut.\nFür die Ebenengleichung der Form: ax + by + cz = d")
                    pl_coord_a = 0
                    pl_coord_b = 0
                    pl_coord_c = 0
                    pl_coord_d = 0
                    pl_coord_correct = False
                    pl_coord_confirm = False
                    pl_coord_confirm_no = False
                    while not pl_coord_confirm:
                        while (not pl_coord_correct) or pl_coord_confirm:
                            # a
                            pl_coord_a_understand = False
                            while not pl_coord_a_understand:
                                try:
                                    pl_coord_a = float(input("Was ist a: "))
                                    pl_coord_a_understand = True
                                except ValueError:
                                    print(misunderstand[random.randint(0, len(misunderstand) - 1)])
                            # b
                            pl_coord_b_understand = False
                            while not pl_coord_b_understand:
                                try:
                                    pl_coord_b = float(input("Was ist b: "))
                                    pl_coord_b_understand = True
                                except ValueError:
                                    print(misunderstand[random.randint(0, len(misunderstand) - 1)])
                            # c
                            pl_coord_c_understand = False
                            while not pl_coord_c_understand:
                                try:
                                    pl_coord_c = float(input("Was ist c: "))
                                    pl_coord_c_understand = True
                                except ValueError:
                                    print(misunderstand[random.randint(0, len(misunderstand) - 1)])
                            # d
                            pl_coord_d_understand = False
                            while not pl_coord_d_understand:
                                try:
                                    pl_coord_d = float(input("Was ist d: "))
                                    pl_coord_d_understand = True
                                except ValueError:
                                    print(misunderstand[random.randint(0, len(misunderstand) - 1)])
                            if Calc.Vector(pl_coord_a, pl_coord_b, pl_coord_c).fullzero:
                                print("Diese Gleichung beschreibt keine Ebene."
                                      "\nVersuchen wir das nochmal.")
                                pl_coord_correct = False
                            else:
                                pl_coord_correct = True
                        # confirm
                        print("Also die Ebene:\n(" + str(pl_coord_a) + ")x + (" + str(pl_coord_b) + ")y + (" +
                              str(pl_coord_c) + ")z = " + str(pl_coord_d) + " ?")
                        while not pl_coord_confirm:
                            user_pl_coord_confirm = input().upper()
                            for ii in user_boolean:
                                for jj in ii:
                                    if user_pl_coord_confirm == jj:
                                        if user_boolean.index(ii) == 0:
                                            pl_coord_confirm = True
                                        elif user_boolean.index(ii) == 1:
                                            pl_coord_confirm_no = True
                                            pl_coord_correct = False
                                            print("Okay, versuchen wir das nochmal.")
                            if not (pl_coord_confirm_no or pl_coord_confirm):
                                print(misunderstand[random.randint(0, len(misunderstand) - 1)])
                            if pl_coord_confirm_no:
                                break
                    object_1 = stage_2_pl_coord(pl_coord_a, pl_coord_b, pl_coord_c, pl_coord_d)
                    self.obj_calc.append(object_1)
                elif obj_pl_type == 3:
                    print("Verstehe.")
                    pl_pt_aa_x = 0
                    pl_pt_aa_y = 0
                    pl_pt_aa_z = 0
                    pl_pt_bb_x = 0
                    pl_pt_bb_y = 0
                    pl_pt_bb_z = 0
                    pl_pt_cc_x = 0
                    pl_pt_cc_y = 0
                    pl_pt_cc_z = 0
                    pl_pt_correct = False
                    while not pl_pt_correct:
                        # aa
                        pl_pt_aa_confirm = False
                        pl_pt_aa_confirm_no = False
                        while not pl_pt_aa_confirm:
                            pl_pt_aa_x_understand = False
                            while not pl_pt_aa_x_understand:
                                try:
                                    pl_pt_aa_x = float(input("Wie lautet dein erster Punkt(x-Koordinate): "))
                                    pl_pt_aa_x_understand = True
                                except ValueError:
                                    print(misunderstand[random.randint(0, len(misunderstand) - 1)])
                            pl_pt_aa_y_understand = False
                            while not pl_pt_aa_y_understand:
                                try:
                                    pl_pt_aa_y = float(input("Wie lautet dein erster Punkt(y-Koordinate): "))
                                    pl_pt_aa_y_understand = True
                                except ValueError:
                                    print(misunderstand[random.randint(0, len(misunderstand) - 1)])
                            pl_pt_aa_z_understand = False
                            while not pl_pt_aa_z_understand:
                                try:
                                    pl_pt_aa_z = float(input("Wie lautet dein erster Punkt(z-Koordinate): "))
                                    pl_pt_aa_z_understand = True
                                except ValueError:
                                    print(misunderstand[random.randint(0, len(misunderstand) - 1)])
                            # aa_confirm
                            print("Also Punkt A(" + str(pl_pt_aa_x) + "|" + str(pl_pt_aa_y) + "|" +
                                  str(pl_pt_aa_z) + ")?")
                            while not pl_pt_aa_confirm:
                                user_pl_aa_confirm = input().upper()
                                for ii in user_boolean:
                                    for jj in ii:
                                        if user_pl_aa_confirm == jj:
                                            if user_boolean.index(ii) == 0:
                                                pl_pt_aa_confirm = True
                                                print("Gut.")
                                            elif user_boolean.index(ii) == 1:
                                                pl_pt_aa_confirm_no = True
                                                print("Okay, versuchen wir das nochmal.")
                                if not (pl_pt_aa_confirm_no or pl_pt_aa_confirm):
                                    print(misunderstand[random.randint(0, len(misunderstand) - 1)])
                                if pl_pt_aa_confirm_no:
                                    break
                        # bb
                        pl_pt_bb_confirm = False
                        pl_pt_bb_confirm_no = False
                        while not pl_pt_bb_confirm:
                            pl_pt_bb_x_understand = False
                            while not pl_pt_bb_x_understand:
                                try:
                                    pl_pt_bb_x = float(input("Wie lautet dein zweiter Punkt(x-Koordinate): "))
                                    pl_pt_bb_x_understand = True
                                except ValueError:
                                    print(misunderstand[random.randint(0, len(misunderstand) - 1)])
                            pl_pt_bb_y_understand = False
                            while not pl_pt_bb_y_understand:
                                try:
                                    pl_pt_bb_y = float(input("Wie lautet dein zweiter Punkt(y-Koordinate): "))
                                    pl_pt_bb_y_understand = True
                                except ValueError:
                                    print(misunderstand[random.randint(0, len(misunderstand) - 1)])
                            pl_pt_bb_z_understand = False
                            while not pl_pt_bb_z_understand:
                                try:
                                    pl_pt_bb_z = float(input("Wie lautet dein zweiter Punkt(z-Koordinate): "))
                                    pl_pt_bb_z_understand = True
                                except ValueError:
                                    print(misunderstand[random.randint(0, len(misunderstand) - 1)])
                            # bb_confirm
                            print("Also Punkt B(" + str(pl_pt_bb_x) + "|" + str(pl_pt_bb_y) + "|" +
                                  str(pl_pt_bb_z) + ")?")
                            while not pl_pt_bb_confirm:
                                user_pl_bb_confirm = input().upper()
                                for ii in user_boolean:
                                    for jj in ii:
                                        if user_pl_bb_confirm == jj:
                                            if user_boolean.index(ii) == 0:
                                                print("Gut.")
                                                pl_pt_bb_confirm = True
                                            elif user_boolean.index(ii) == 1:
                                                pl_pt_bb_confirm_no = True
                                                print("Okay, versuchen wir das nochmal.")
                                if not (pl_pt_bb_confirm_no or pl_pt_bb_confirm):
                                    print(misunderstand[random.randint(0, len(misunderstand) - 1)])
                                if pl_pt_bb_confirm_no:
                                    break
                        # cc
                        pl_pt_cc_confirm = False
                        pl_pt_cc_confirm_no = False
                        while not pl_pt_cc_confirm:
                            pl_pt_cc_x_understand = False
                            while not pl_pt_cc_x_understand:
                                try:
                                    pl_pt_cc_x = float(input("Wie lautet dein dritter Punkt(x-Koordinate): "))
                                    pl_pt_cc_x_understand = True
                                except ValueError:
                                    print(misunderstand[random.randint(0, len(misunderstand) - 1)])
                            pl_pt_cc_y_understand = False
                            while not pl_pt_cc_y_understand:
                                try:
                                    pl_pt_cc_y = float(input("Wie lautet dein dritter Punkt(y-Koordinate): "))
                                    pl_pt_cc_y_understand = True
                                except ValueError:
                                    print(misunderstand[random.randint(0, len(misunderstand) - 1)])
                            pl_pt_cc_z_understand = False
                            while not pl_pt_cc_z_understand:
                                try:
                                    pl_pt_cc_z = float(input("Wie lautet dein dritter Punkt(z-Koordinate): "))
                                    pl_pt_cc_z_understand = True
                                except ValueError:
                                    print(misunderstand[random.randint(0, len(misunderstand) - 1)])
                            # cc_confirm
                            print("Also Punkt C(" + str(pl_pt_cc_x) + "|" + str(pl_pt_cc_y) + "|" +
                                  str(pl_pt_cc_z) + ")?")
                            while not pl_pt_cc_confirm:
                                user_pl_cc_confirm = input().upper()
                                for ii in user_boolean:
                                    for jj in ii:
                                        if user_pl_cc_confirm == jj:
                                            if user_boolean.index(ii) == 0:
                                                pl_pt_cc_confirm = True
                                            elif user_boolean.index(ii) == 1:
                                                pl_pt_cc_confirm_no = True
                                                print("Okay, versuchen wir das nochmal.")
                                if not (pl_pt_cc_confirm_no or pl_pt_cc_confirm):
                                    print(misunderstand[random.randint(0, len(misunderstand) - 1)])
                                if pl_pt_cc_confirm_no:
                                    break
                        try:
                            object_1 = stage_2_pl_pt(Calc.Point(pl_pt_aa_x, pl_pt_aa_y, pl_pt_aa_z),
                                                     Calc.Point(pl_pt_bb_x, pl_pt_bb_y, pl_pt_bb_z),
                                                     Calc.Point(pl_pt_cc_x, pl_pt_cc_y, pl_pt_cc_z))
                            self.obj_calc.append(object_1)
                            pl_pt_correct = True
                            print("Perfekt.")
                        except SystemExit:
                            print("Diese Punkte beschreiben keine eindeutige Ebene\nVersuchen wir das nochmal.")
            name_i += 1


# Stage 0 & 1


def stage_1_dis():
    print("Abstände? Da weiß ich bescheid!")
    chosen_object1 = 0
    chosen_object2 = 0
    user_object1_understand = False
    while not user_object1_understand:
        user_dis_obj1 = input("Zwischen welchen Objekten brauchst du den Abstand(Objekt 1)?\n").upper()
        for object_list in object_full_list:
            for single_object in object_list:
                if user_dis_obj1 == single_object and not (object_list == object_vector):
                    user_object1_understand = True
                    chosen_object1 = object_full_list.index(object_list)
        if not user_object1_understand:
            print(misunderstand[random.randint(0, len(misunderstand) - 1)])

    print("Okay verstehe.")
    user_object2_understand = False
    while not user_object2_understand:
        user_dis_obj2 = input("Was ist denn das zweite Objekt(Objekt 2)?\n").upper()
        for object_list in object_full_list:
            for single_object in object_list:
                if user_dis_obj2 == single_object and not (object_list == object_vector):
                    user_object2_understand = True
                    chosen_object2 = object_full_list.index(object_list)
        if not user_object2_understand:
            print(misunderstand[random.randint(0, len(misunderstand) - 1)])

    chosen_objects = [chosen_object1, chosen_object2]
    return chosen_objects


def stage_1_cross():
    print("Schnittmengen? Da kann ich dir helfen!")
    chosen_object1 = 0
    chosen_object2 = 0
    user_object1_understand = False
    while not user_object1_understand:
        user_dis_obj1 = input("Zwischen welchen zwei Objekten brauchst du die Schnittmenge(Objekt 1)?\n").upper()
        for object_list in object_full_list:
            for single_object in object_list:
                if user_dis_obj1 == single_object and (object_list == object_line or object_list == object_plane):
                    user_object1_understand = True
                    chosen_object1 = object_full_list.index(object_list)
        if not user_object1_understand:
            print(misunderstand[random.randint(0, len(misunderstand) - 1)])

    print("Okay gut.")
    user_object2_understand = False
    while not user_object2_understand:
        user_dis_obj2 = input("Was ist denn das zweite Objekt(Objekt 2)?\n")
        for object_list in object_full_list:
            for single_object in object_list:
                if user_dis_obj2.upper() == single_object and \
                        (object_list == object_line or object_list == object_plane):
                    user_object2_understand = True
                    chosen_object2 = object_full_list.index(object_list)
        if not user_object2_understand:
            print(misunderstand[random.randint(0, len(misunderstand) - 1)])

    chosen_objects = [chosen_object1, chosen_object2]
    return chosen_objects


def stage_1_contain():
    print("Lagebeziehungen? Da helfe ich dir!")
    chosen_object1 = 0
    chosen_object2 = 0
    user_object1_understand = False
    while not user_object1_understand:
        user_dis_obj1 = input("Zwischen welchen zwei Objekten brauchst du die Lagebeziehung(Objekt 1)?\n").upper()
        for object_list in object_full_list:
            for single_object in object_list:
                if user_dis_obj1 == single_object and not (object_list == object_vector):
                    user_object1_understand = True
                    chosen_object1 = object_full_list.index(object_list)
        if not user_object1_understand:
            print(misunderstand[random.randint(0, len(misunderstand) - 1)])

    print("Passt.")
    user_object2_understand = False
    while not user_object2_understand:
        user_dis_obj2 = input("Was ist denn das zweite Objekt(Objekt 2)?\n")
        for object_list in object_full_list:
            for single_object in object_list:
                if user_dis_obj2.upper() == single_object and not (object_list == object_vector):
                    user_object2_understand = True
                    chosen_object2 = object_full_list.index(object_list)
        if not user_object2_understand:
            print(misunderstand[random.randint(0, len(misunderstand) - 1)])

    chosen_objects = [chosen_object1, chosen_object2]
    return chosen_objects


def stage_0(iteration):
    user_topic = input("Zu was hast du denn deine " + str(iteration) + ". Frage?\n").upper()
    chosen_topic = 0
    user_topic_understand = False
    for answer_list in topic:
        for answer in answer_list:
            if user_topic == answer:
                user_topic_understand = True
                chosen_topic = topic.index(answer_list)

    while not user_topic_understand:
        print("Ich weiß nicht was du meinst. Vielleicht weißt du auch nicht, was ich meine.")
        print("Ich kann dir gerne helfen, wenn es um Abstände, Schnittmengen, Lagebeziehungen oder allgemeine "
              "Grundsachen geht.")
        user_topic = input("In welchem Bereich brauchst du Hilfe?\n").upper()
        for answer_list in topic:
            for answer in answer_list:
                if user_topic == answer:
                    user_topic_understand = True
                    chosen_topic = topic.index(answer_list)
    return chosen_topic


def stage_1(chosen_topic, task_name):
    if chosen_topic == 0:
        stage1 = stage_1_dis()
        chosen_task = Task(task_name, chosen_topic, stage1[0], stage1[1])
        task_list.append(chosen_task)
    elif chosen_topic == 1:
        stage1 = stage_1_cross()
        chosen_task = Task(task_name, chosen_topic, stage1[0], stage1[1])
        task_list.append(chosen_task)
    elif chosen_topic == 2:
        stage1 = stage_1_contain()
        chosen_task = Task(task_name, chosen_topic, stage1[0], stage1[1])
        task_list.append(chosen_task)


# Chat Start
print("Hallo, ich bin " + program_name + ". Wie heißt du?")
username = input()
misunderstand = [username + ", ich weiß nicht genau, was du meinst.", "Was meinst du damit?", "Das verstehe ich nicht.",
                 "Das habe ich nicht verstanden.", "Wie meinst du das?"]
print("Schön von dir zu hören, " + username + "!")
print("Du bist hier, um über Mathe zu reden? Freut mich!")
print("Von mir aus können wir gerne stundenlang über Schnittmengen, Abstände, Lagebeziehungen und weiteres sprechen!")
iterate_understand = False
iterate = 0
while not iterate_understand:
    try:
        iterate = int(input("Wie viele Fragen hast du für mich?\n"))
        iterate_understand = True
    except ValueError:
        print(misunderstand[random.randint(0, len(misunderstand) - 1)])

for i in range(iterate):
    user_chosen_topic = stage_0(i + 1)
    name = "Frage " + str(i + 1)
    stage_1(user_chosen_topic, name)

'''
Testing:

for j in task_list:
    j.obj_define()
    for k in j.obj_calc:
        print("\n" + j.task_name)
        print(k.a)
        print(k.b)
        print(k.c)
        print(k.d)
'''
