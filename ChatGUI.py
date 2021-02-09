import sys
import Calc
import BasicMath
import random
from math import *
import datetime

'''
Todo:
- custom input
- basic calc file
'''
'''
Stages:
0 == Introduction - Topic chosen
1 == Objects asked - Objects chosen - task_list filled
2 == for object in task_list: Chosen objects defined as Calc.py-objects
3 == for object in task_list: Chosen methods defined as Calc.py-methods
4 == for object in task_list: Solution calculated
5 == for object in task_list: Calc.py-solution defined into words
6 == for object in task_list: Solution returned
7 == Repeat or End
'''
# Meta Var
program_name = "Mathemann"
programmer_name = "Blind Fish"
date = str(datetime.date.today())
# Choice Arrays
task_list = []

misunderstand = ["Was meinst du damit?", "Das verstehe ich nicht.", "Das habe ich nicht verstanden.",
                 "Wie meinst du das?"]

user_true = ["JA", "KLAR", "JUP", "JAP", "GENAU", "RICHTIG", "KORREKT", "PASST", "CHECK", "SURE"]
user_false = ["NEIN", "NE", "NICHT", "FALSCH", "UNGENAU"]
user_boolean = [user_true, user_false]

basic_plus = ["PLUS", "PLUSRECHNEN", "PLUS RECHNEN", "ADDITION", "ADDIEREN", "SUMME"]
basic_minus = ["MINUS", "MINUSRECHNEN", "MINUS RECHNEN", "DIFFERENZ", "DIFFERENZIEREN"]
basic_scalar_multi = ["SKALARMULTIPLIKATION", "SKALIEREN", "SKALIERUNG", "SKALIERT"]
basic_scalar_product = ["SKALARPRODUKT"]
basic_vector_product = ["VEKTORPRODUKT", "KREUZPRODUKT"]
basic_spar_product = ["SPATPRODUKT", "SPAT"]
basic_unit = ["EINHEITSVEKTOR", "BASISVEKTOR"]
basic_ld = ["LINEARE ABHÄNGIGKEIT", "ABHÄNGIGKEIT", "LINEAR ABHÄNGIG"]
basic_convert = ["UMWANDLUNG", "UMWANDELN", "UMFORMUNG", "UMFORMEN", "UMRECHNUNG", "UMRECHNEN"]
basic_method = [basic_plus, basic_minus, basic_scalar_multi, basic_scalar_product, basic_vector_product,
                basic_spar_product, basic_unit, basic_ld, basic_convert]

topic_basic = ["Grundrechnung", "SKALAR", "MAL"]
for basic_method_type in basic_method:
    for basic_method_keyword in basic_method_type:
        topic_basic.append(basic_method_keyword)
topic_dis = ["Abstand", "ABSTAND", "ABSTÄNDE", "DISTANZ", "DISTANZEN", "ENTFERNUNG", "ENTFERNUNGEN"]
topic_cross = ["Schnittmenge", "SCHNITTPUNKT", "SCHNITTPUNKTE", "SCHNITTGERADE", "SCHNITTGERADEN", "SCHNITTMENGE",
               "SCHNITTMENGEN"]
topic_contain = ["Lagebeziehung", "LAGEBEZIEHUNG", "LAGEBEZIEHUNGEN", "LAGEVERHÄLTNIS", "LAGE"]
topic = [topic_dis, topic_cross, topic_contain, topic_basic]

object_point = ["Punkt", "PUNKT", "."]
object_line = ["Gerade", "GERADE", "LINIE", "STRICH"]
object_plane = ["Ebene", "EBENE", "FLÄCHE", "OBERFLÄCHE"]
object_vector = ["Vektor", "VEKTOR", "RICHTUNG"]
object_full_list = [object_point, object_line, object_plane, object_vector]

object_type_pt_pt = ["PUNKT", "PUNKTE"]
object_type_pt = [object_type_pt_pt]

object_type_vc_vc = ["VEKTOR", "VEKTOREN"]
object_type_vc = [object_type_vc_vc]

object_type_ln_pt = ["PUNKT", "PUNKTE", "GRUPPE VON MEHREREN PUNKTEN", "GRUPPE VON ZWEI PUNKTEN",
                     "MEHRERE PUNKTE", "ZWEI PUNKTE", "2 PUNKTE", "."]
object_type_ln_par = ["PARAMETER", "PARAMETERFORM", "VEKTOR", "VEKTOREN", "RICHTUNGSVEKTOR", "RICHTUNGSVEKTOREN"]
object_type_ln = [object_type_ln_par, object_type_ln_pt]

object_type_pl_par = ["PARAMETER", "PARAMETERFORM", "VEKTOR", "VEKTOREN", "RICHTUNGSVEKTOR", "RICHTUNGSVEKTOREN",
                      "SPANNVEKTOR", "SPANNVEKTOREN"]
object_type_pl_norm = ["NORMAL", "NORMALE", "NORMALENFORM"]
object_type_pl_coord = ["KOORDINATE", "KOORDINATEN", "KOORDINATENFORM", "COORDS", "COORD"]
object_type_pl_pt = ["PUNKT", "PUNKTE", "GRUPPE VON MEHREREN PUNKTEN", "MEHRERE PUNKTE", "DREI PUNKTE", "3 PUNKTE", "."]
object_type_pl = [object_type_pl_par, object_type_pl_norm, object_type_pl_coord, object_type_pl_pt]

object_type_full_list = [object_type_pt, object_type_ln, object_type_pl, object_type_vc]

# Warning: Strangers with the same name
# Warning: Names and birth dates in public code
common_names = [["ADRIAN", "YYYY-05-24"], ["BLIND FISH", "YYYY-05-24"], ["BF", "YYYY-05-24"],
                ["JOHANNES", "YYYY-MM-DD"], ["MARVIN", "YYYY-05-12"], ["LOGIKERUS", "YYYY-05-12"],
                ["ELLI", "YYYY-12-08"], ["ELISABETH", "YYYY-12-08"], ["DILARA", "YYYY-01-29"],
                ["JAMILA", "YYYY-01-17"]]


# date check
def date_check(custom_date):
    date_overlap = True
    for i in range(5, 10, 1):
        if custom_date[i] != date[i]:
            date_overlap = False
            return date_overlap
    return date_overlap


# Common Name & Intro
def name_input(username_input):  # Sort through any known name for a special greeting
    user_text = str(username_input)
    birthday = False
    greeting = str("Schön von dir zu hören, " + str(user_text) +
                   "!\nDu bist hier, um über Mathe zu reden? Freut mich!\n"
                   "Von mir aus können wir gerne stundenlang über "
                   "Schnittmengen, Abstände, Lagebeziehungen und weiteres sprechen!")
    for ii in common_names:
        if user_text.upper() == ii[0]:
            if common_names.index(ii) == 0 or common_names.index(ii) == 1 or common_names.index(ii) == 2:
                greeting = str("Ah, man sieht sich wieder, " + user_text + "."
                               + "\nBrauchst du meine Hilfe oder willst du mich wieder testen?\n"
                                 "Ist ja auch egal, ich bin sowieso bestens vorbereitet "
                                 "aber das weißt du ja besser als ich.")
                birthday = date_check(ii[1])
            elif common_names.index(ii) == 3:
                greeting = str("Oh hi " + user_text + ". Ich bin etwas überrascht von dir zu hören."
                               + "\nIch habe gehört, dass du meine Hilfe "
                                 "für deine Hausaufgaben nicht haben möchtest.\n"
                                 "Hast du dich umentschieden? Ich könnte dir beispielsweise bei "
                                 "Schnittmengen, Abständen, Lagebeziehungen oder Umformungen eine Hilfe sein.")
                birthday = date_check(ii[1])
            elif common_names.index(ii) == 4 or common_names.index(ii) == 5:
                greeting = str(user_text + "? Schön von dir zu hören!"
                               + "\nDass du Mathe-Fragen hast überrascht mich etwas.\n"
                                 "Worum geht es denn heute? Schnittmengen, Abstände, Lagebeziehungen, Umformungen "
                                 "oder vielleicht doch was anderes?")
                birthday = date_check(ii[1])
            elif common_names.index(ii) == 6 or common_names.index(ii) == 7:
                greeting = str("Schön von dir zu hören, " + str(user_text) +
                               "!\nBist du hier um die Lösung deiner Hausaufgaben zu überprüfen? "
                               "Mein Gefühl sagt mir, dass du alles schon richtig hast, aber mal sehen.\n"
                               "Worum geht es denn in den Aufgaben von heute? Schnittmengen, "
                               "Abstände, Lagebeziehungen, Umformungen oder vielleicht doch was anderes?")
                birthday = date_check(ii[1])
            elif common_names.index(ii) == 8:
                birthday = date_check(ii[1])
            elif common_names.index(ii) == 9:
                birthday = date_check(ii[1])
    if birthday:
        greeting = str("Hi " + user_text + "! Herzlichen Glückwunsch zum Geburtstag!"
                       + "\nHoffentlich konntest du heute schöneres machen als über Mathe nachzudenken.\n"
                         "Weil ich dich dafür aber besser kennen lernen kann, können wir von mir aus gerne über"
                         " Schnittmengen, Abstände, Lagebeziehungen und weiteres sprechen!")
    return greeting


# Intro
username = str(input("Hallo, ich bin " + program_name + ". Wie heißt du?\n"))
username_help = str(username) + " "
if username_help.isspace():
    print("Kann es sein, dass du keinen Namen hast? Naja egal.\n")
    username = "Mathematik-Fan"
misunderstand.append(username + ", ich weiß nicht genau was du meinst.")
print(name_input(username))


# Task 2
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


def stage_2_line():
    ln_understand = False
    print("In welcher Form kennst du diese Gerade?")
    ln_type = 0
    while not ln_understand:
        user_ln_type = input().upper()
        for ii in object_type_ln:
            for jj in ii:
                if user_ln_type == jj:
                    ln_understand = True
                    ln_type = object_type_ln.index(ii)
        if not ln_understand:
            print(misunderstand[random.randint(0, len(misunderstand) - 1)] +
                  "\nIn welcher Form kennst du diese Gerade? In der Parameterform oder als Gruppe von zwei Punkten?")
    return ln_type


def stage_2_pl_pt(pl_pt_aa, pl_pt_bb, pl_pt_cc):
    output = Calc.Plane(Calc.Conv.Pl.Pt.par(pl_pt_aa, pl_pt_bb, pl_pt_cc)[0],
                        Calc.Conv.Pl.Pt.par(pl_pt_aa, pl_pt_bb, pl_pt_cc)[1],
                        Calc.Conv.Pl.Pt.par(pl_pt_aa, pl_pt_bb, pl_pt_cc)[2])
    return output


def stage_2_pl_coord(a, b, c, d):
    output = Calc.Plane(Calc.Conv.Pl.Coord.par(a, b, c, d)[0], Calc.Conv.Pl.Coord.par(a, b, c, d)[1],
                        Calc.Conv.Pl.Coord.par(a, b, c, d)[2])
    return output


def stage_2_pl_norm(sp, normal):
    if normal.fullzero:
        sys.exit("Ein Normalvektor ohne Richtung kann keine Ebene eindeutig beschreiben.")
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


def stage_2_def_c():
    c = 0
    c_confirm = False
    while not c_confirm:
        c_confirm_no = False
        c_understand = False
        while not c_understand:
            c_understand = False
            try:
                c = float(input("Was ist deine Konstante: "))
                c_understand = True
            except ValueError:
                print(misunderstand[random.randint(0, len(misunderstand) - 1)])
        print("Also die Konstante " + str(c) + "?")
        while not c_confirm:
            user_c_confirm = input().upper()
            for ii in user_boolean:
                for jj in ii:
                    if user_c_confirm == jj:
                        if user_boolean.index(ii) == 0:
                            c_confirm = True
                        elif user_boolean.index(ii) == 1:
                            c_confirm_no = True
                            print("Okay, versuchen wir das nochmal.")
            if not (c_confirm_no or c_confirm):
                print(misunderstand[random.randint(0, len(misunderstand) - 1)])
            if c_confirm_no:
                break
    return c


def stage_2_def_vc():
    vc_x = 0
    vc_y = 0
    vc_z = 0
    # Vector
    vc_confirm = False
    while not vc_confirm:
        vc_confirm_no = False
        vc_x_understand = False
        while not vc_x_understand:
            try:
                vc_x = float(input("In welche Richtung zeigt der Vektor(x-Koordinate): "))
                vc_x_understand = True
            except ValueError:
                print(misunderstand[random.randint(0, len(misunderstand) - 1)])
        vc_y_understand = False
        while not vc_y_understand:
            try:
                vc_y = float(input("In welche Richtung zeigt der Vektor(y-Koordinate): "))
                vc_y_understand = True
            except ValueError:
                print(misunderstand[random.randint(0, len(misunderstand) - 1)])
        vc_z_understand = False
        while not vc_z_understand:
            try:
                vc_z = float(input("In welche Richtung zeigt der Vektor(z-Koordinate): "))
                vc_z_understand = True
            except ValueError:
                print(misunderstand[random.randint(0, len(misunderstand) - 1)])
        # vc_confirm
        print("Also ein Vektor mit diesen Koordinaten (" + str(vc_x) + "|" + str(vc_y) + "|" +
              str(vc_z) + ")?")
        if Calc.Vector(vc_x, vc_y, vc_z).fullzero:
            print("Achtung: Dieser Vektor hat eine Länge von 0 Längeneinheiten.")
        while not vc_confirm:
            user_vc_confirm = input().upper()
            for ii in user_boolean:
                for jj in ii:
                    if user_vc_confirm == jj:
                        if user_boolean.index(ii) == 0:
                            vc_confirm = True
                        elif user_boolean.index(ii) == 1:
                            vc_confirm_no = True
                            print("Okay, versuchen wir das nochmal.")
            if not (vc_confirm_no or vc_confirm):
                print(misunderstand[random.randint(0, len(misunderstand) - 1)])
            if vc_confirm_no:
                break
    return [vc_x, vc_y, vc_z]


def stage_2_def_pt():
    pt_x = 0
    pt_y = 0
    pt_z = 0
    # Point
    pt_confirm = False
    while not pt_confirm:
        pt_confirm_no = False
        pt_x_understand = False
        while not pt_x_understand:
            try:
                pt_x = float(input("Wo ist der Punkt(x-Koordinate): "))
                pt_x_understand = True
            except ValueError:
                print(misunderstand[random.randint(0, len(misunderstand) - 1)])
        pt_y_understand = False
        while not pt_y_understand:
            try:
                pt_y = float(input("Wo ist der Punkt(y-Koordinate): "))
                pt_y_understand = True
            except ValueError:
                print(misunderstand[random.randint(0, len(misunderstand) - 1)])
        pt_z_understand = False
        while not pt_z_understand:
            try:
                pt_z = float(input("Wo ist der Punkt(z-Koordinate): "))
                pt_z_understand = True
            except ValueError:
                print(misunderstand[random.randint(0, len(misunderstand) - 1)])
        # pt_confirm
        print("Also ein Punkt mit diesen Koordinaten (" + str(pt_x) + "|" + str(pt_y) + "|" +
              str(pt_z) + ")?")
        while not pt_confirm:
            user_pt_confirm = input().upper()
            for ii in user_boolean:
                for jj in ii:
                    if user_pt_confirm == jj:
                        if user_boolean.index(ii) == 0:
                            pt_confirm = True
                        elif user_boolean.index(ii) == 1:
                            pt_confirm_no = True
                            print("Okay, versuchen wir das nochmal.")
            if not (pt_confirm_no or pt_confirm):
                print(misunderstand[random.randint(0, len(misunderstand) - 1)])
            if pt_confirm_no:
                break
    return [pt_x, pt_y, pt_z]


def stage_2_def_ln_par():
    ln_par_sp_x = 0
    ln_par_sp_y = 0
    ln_par_sp_z = 0
    ln_par_dr_x = 0
    ln_par_dr_y = 0
    ln_par_dr_z = 0
    ln_par_correct = False
    while not ln_par_correct:
        # Support
        ln_par_sp_confirm = False
        while not ln_par_sp_confirm:
            ln_par_sp_confirm_no = False
            ln_par_sp_x_understand = False
            while not ln_par_sp_x_understand:
                try:
                    ln_par_sp_x = float(input("Wie lautet dein Stützvektor(x-Koordinate): "))
                    ln_par_sp_x_understand = True
                except ValueError:
                    print(misunderstand[random.randint(0, len(misunderstand) - 1)])
            ln_par_sp_y_understand = False
            while not ln_par_sp_y_understand:
                try:
                    ln_par_sp_y = float(input("Wie lautet dein Stützvektor(y-Koordinate): "))
                    ln_par_sp_y_understand = True
                except ValueError:
                    print(misunderstand[random.randint(0, len(misunderstand) - 1)])
            ln_par_sp_z_understand = False
            while not ln_par_sp_z_understand:
                try:
                    ln_par_sp_z = float(input("Wie lautet dein Stützvektor(z-Koordinate): "))
                    ln_par_sp_z_understand = True
                except ValueError:
                    print(misunderstand[random.randint(0, len(misunderstand) - 1)])
            # sp_confirm
            print("Also Stützvektor s = (" + str(ln_par_sp_x) + "|" + str(ln_par_sp_y) + "|" +
                  str(ln_par_sp_z) + ")?")
            while not ln_par_sp_confirm:
                user_ln_sp_confirm = input().upper()
                for ii in user_boolean:
                    for jj in ii:
                        if user_ln_sp_confirm == jj:
                            if user_boolean.index(ii) == 0:
                                ln_par_sp_confirm = True
                                print("Gut.")
                            elif user_boolean.index(ii) == 1:
                                ln_par_sp_confirm_no = True
                                print("Okay, versuchen wir das nochmal.")
                if not (ln_par_sp_confirm_no or ln_par_sp_confirm):
                    print(misunderstand[random.randint(0, len(misunderstand) - 1)])
                if ln_par_sp_confirm_no:
                    break
        # Direction
        ln_par_dr_confirm = False
        while not ln_par_dr_confirm:
            ln_par_dr_confirm_no = False
            ln_par_dr_x_understand = False
            while not ln_par_dr_x_understand:
                try:
                    ln_par_dr_x = float(
                        input("Wie lautet dein Richtungsvektor(x-Koordinate): "))
                    ln_par_dr_x_understand = True
                except ValueError:
                    print(misunderstand[random.randint(0, len(misunderstand) - 1)])
            ln_par_dr_y_understand = False
            while not ln_par_dr_y_understand:
                try:
                    ln_par_dr_y = float(
                        input("Wie lautet dein Richtungsvektor(y-Koordinate): "))
                    ln_par_dr_y_understand = True
                except ValueError:
                    print(misunderstand[random.randint(0, len(misunderstand) - 1)])
            ln_par_dr_z_understand = False
            while not ln_par_dr_z_understand:
                try:
                    ln_par_dr_z = float(
                        input("Wie lautet dein Richtungsvektor(z-Koordinate): "))
                    ln_par_dr_z_understand = True
                except ValueError:
                    print(misunderstand[random.randint(0, len(misunderstand) - 1)])
            # dr_confirm
            print(
                "Also Richtungsvektor r = (" + str(ln_par_dr_x) + "|" + str(ln_par_dr_y) + "|" +
                str(ln_par_dr_z) + ")?")
            while not ln_par_dr_confirm:
                user_ln_dr_confirm = input().upper()
                for ii in user_boolean:
                    for jj in ii:
                        if user_ln_dr_confirm == jj:
                            if user_boolean.index(ii) == 0:
                                ln_par_dr_confirm = True
                            elif user_boolean.index(ii) == 1:
                                ln_par_dr_confirm_no = True
                                print("Okay, versuchen wir das nochmal.")
                if not (ln_par_dr_confirm_no or ln_par_dr_confirm):
                    print(misunderstand[random.randint(0, len(misunderstand) - 1)])
                if ln_par_dr_confirm_no:
                    break
        try:
            stage_2_ln_par(Calc.Vector(ln_par_sp_x, ln_par_sp_y, ln_par_sp_z),
                           Calc.Vector(ln_par_dr_x, ln_par_dr_y, ln_par_dr_z))
            ln_par_correct = True
        except SystemExit:
            print("Diese Vektoren beschreiben keine eindeutige Gerade."
                  "\nVersuchen wir das nochmal.")
    return [ln_par_sp_x, ln_par_sp_y, ln_par_sp_z, ln_par_dr_x, ln_par_dr_y, ln_par_dr_z]


def stage_2_def_ln_pt():
    ln_pt_aa_x = 0
    ln_pt_aa_y = 0
    ln_pt_aa_z = 0
    ln_pt_bb_x = 0
    ln_pt_bb_y = 0
    ln_pt_bb_z = 0
    ln_pt_correct = False
    while not ln_pt_correct:
        # aa
        ln_pt_aa_confirm = False
        while not ln_pt_aa_confirm:
            ln_pt_aa_confirm_no = False
            ln_pt_aa_x_understand = False
            while not ln_pt_aa_x_understand:
                try:
                    ln_pt_aa_x = float(input("Wo ist dein erster Punkt(x-Koordinate): "))
                    ln_pt_aa_x_understand = True
                except ValueError:
                    print(misunderstand[random.randint(0, len(misunderstand) - 1)])
            ln_pt_aa_y_understand = False
            while not ln_pt_aa_y_understand:
                try:
                    ln_pt_aa_y = float(input("Wo ist dein erster Punkt(y-Koordinate): "))
                    ln_pt_aa_y_understand = True
                except ValueError:
                    print(misunderstand[random.randint(0, len(misunderstand) - 1)])
            ln_pt_aa_z_understand = False
            while not ln_pt_aa_z_understand:
                try:
                    ln_pt_aa_z = float(input("Wo ist dein erster Punkt(z-Koordinate): "))
                    ln_pt_aa_z_understand = True
                except ValueError:
                    print(misunderstand[random.randint(0, len(misunderstand) - 1)])
            # aa_confirm
            print("Also Punkt A(" + str(ln_pt_aa_x) + "|" + str(ln_pt_aa_y) + "|" +
                  str(ln_pt_aa_z) + ")?")
            while not ln_pt_aa_confirm:
                user_ln_aa_confirm = input().upper()
                for ii in user_boolean:
                    for jj in ii:
                        if user_ln_aa_confirm == jj:
                            if user_boolean.index(ii) == 0:
                                ln_pt_aa_confirm = True
                                print("Gut.")
                            elif user_boolean.index(ii) == 1:
                                ln_pt_aa_confirm_no = True
                                print("Okay, versuchen wir das nochmal.")
                if not (ln_pt_aa_confirm_no or ln_pt_aa_confirm):
                    print(misunderstand[random.randint(0, len(misunderstand) - 1)])
                if ln_pt_aa_confirm_no:
                    break
        # bb
        ln_pt_bb_confirm = False
        while not ln_pt_bb_confirm:
            ln_pt_bb_confirm_no = False
            ln_pt_bb_x_understand = False
            while not ln_pt_bb_x_understand:
                try:
                    ln_pt_bb_x = float(
                        input("Wo ist dein zweiter Punkt(x-Koordinate): "))
                    ln_pt_bb_x_understand = True
                except ValueError:
                    print(misunderstand[random.randint(0, len(misunderstand) - 1)])
            ln_pt_bb_y_understand = False
            while not ln_pt_bb_y_understand:
                try:
                    ln_pt_bb_y = float(
                        input("Wo ist dein zweiter Punkt(y-Koordinate): "))
                    ln_pt_bb_y_understand = True
                except ValueError:
                    print(misunderstand[random.randint(0, len(misunderstand) - 1)])
            ln_pt_bb_z_understand = False
            while not ln_pt_bb_z_understand:
                try:
                    ln_pt_bb_z = float(
                        input("Wo ist dein zweiter Punkt(z-Koordinate): "))
                    ln_pt_bb_z_understand = True
                except ValueError:
                    print(misunderstand[random.randint(0, len(misunderstand) - 1)])
            # bb_confirm
            print(
                "Also Punkt B(" + str(ln_pt_bb_x) + "|" + str(ln_pt_bb_y) + "|" +
                str(ln_pt_bb_z) + ")?")
            while not ln_pt_bb_confirm:
                user_ln_bb_confirm = input().upper()
                for ii in user_boolean:
                    for jj in ii:
                        if user_ln_bb_confirm == jj:
                            if user_boolean.index(ii) == 0:
                                ln_pt_bb_confirm = True
                            elif user_boolean.index(ii) == 1:
                                ln_pt_bb_confirm_no = True
                                print("Okay, versuchen wir das nochmal.")
                if not (ln_pt_bb_confirm_no or ln_pt_bb_confirm):
                    print(misunderstand[random.randint(0, len(misunderstand) - 1)])
                if ln_pt_bb_confirm_no:
                    break
        try:
            stage_2_ln_pt(Calc.Point(ln_pt_aa_x, ln_pt_aa_y, ln_pt_aa_z),
                          Calc.Point(ln_pt_bb_x, ln_pt_bb_y, ln_pt_bb_z))
            ln_pt_correct = True
        except SystemExit:
            print("Diese Vektoren beschreiben keine eindeutige Gerade."
                  "\nVersuchen wir das nochmal.")
    return [ln_pt_aa_x, ln_pt_aa_y, ln_pt_aa_z, ln_pt_bb_x, ln_pt_bb_y, ln_pt_bb_z]


def stage_2_def_pl_par():
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
        while not pl_par_sp_confirm:
            pl_par_sp_confirm_no = False
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
        while not pl_par_dr1_confirm:
            pl_par_dr1_confirm_no = False
            pl_par_dr1_x_understand = False
            while not pl_par_dr1_x_understand:
                try:
                    pl_par_dr1_x = float(input("Wie lautet dein erster Richtungsvektor(x-Koordinate): "))
                    pl_par_dr1_x_understand = True
                except ValueError:
                    print(misunderstand[random.randint(0, len(misunderstand) - 1)])
            pl_par_dr1_y_understand = False
            while not pl_par_dr1_y_understand:
                try:
                    pl_par_dr1_y = float(input("Wie lautet dein erster Richtungsvektor(y-Koordinate): "))
                    pl_par_dr1_y_understand = True
                except ValueError:
                    print(misunderstand[random.randint(0, len(misunderstand) - 1)])
            pl_par_dr1_z_understand = False
            while not pl_par_dr1_z_understand:
                try:
                    pl_par_dr1_z = float(input("Wie lautet dein erster Richtungsvektor(z-Koordinate): "))
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
        while not pl_par_dr2_confirm:
            pl_par_dr2_confirm_no = False
            pl_par_dr2_x_understand = False
            while not pl_par_dr2_x_understand:
                try:
                    pl_par_dr2_x = float(input("Wie lautet dein zweiter Richtungsvektor(x-Koordinate): "))
                    pl_par_dr2_x_understand = True
                except ValueError:
                    print(misunderstand[random.randint(0, len(misunderstand) - 1)])
            pl_par_dr2_y_understand = False
            while not pl_par_dr2_y_understand:
                try:
                    pl_par_dr2_y = float(input("Wie lautet dein zweiter Richtungsvektor(y-Koordinate): "))
                    pl_par_dr2_y_understand = True
                except ValueError:
                    print(misunderstand[random.randint(0, len(misunderstand) - 1)])
            pl_par_dr2_z_understand = False
            while not pl_par_dr2_z_understand:
                try:
                    pl_par_dr2_z = float(input("Wie lautet dein zweiter Richtungsvektor(z-Koordinate): "))
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
            stage_2_pl_par(Calc.Vector(pl_par_sp_x, pl_par_sp_y, pl_par_sp_z),
                           Calc.Vector(pl_par_dr1_x, pl_par_dr1_y, pl_par_dr1_z),
                           Calc.Vector(pl_par_dr2_x, pl_par_dr2_y, pl_par_dr2_z))
            pl_par_correct = True
        except SystemExit:
            print("Diese Vektoren beschreiben keine eindeutige Ebene.\nVersuchen wir das nochmal.")
    return [pl_par_sp_x, pl_par_sp_y, pl_par_sp_z,
            pl_par_dr1_x, pl_par_dr1_y, pl_par_dr1_z,
            pl_par_dr2_x, pl_par_dr2_y, pl_par_dr2_z]


def stage_2_def_pl_norm():
    pl_norm_sp_x = 0
    pl_norm_sp_y = 0
    pl_norm_sp_z = 0
    pl_norm_norm_x = 0
    pl_norm_norm_y = 0
    pl_norm_norm_z = 0
    pl_norm_correct = False
    while not pl_norm_correct:
        # Support
        pl_norm_sp_confirm = False
        while not pl_norm_sp_confirm:
            pl_norm_sp_confirm_no = False
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
        pl_norm_norm_confirm = False
        while not pl_norm_norm_confirm:
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
            # norm_confirm
            print("Also Normalvektor n = (" + str(pl_norm_norm_x) + "|" + str(pl_norm_norm_y) + "|" +
                  str(pl_norm_norm_z) + ")?")
            while not pl_norm_norm_confirm:
                user_pl_norm_confirm = input().upper()
                for ii in user_boolean:
                    for jj in ii:
                        if user_pl_norm_confirm == jj:
                            if user_boolean.index(ii) == 0:
                                pl_norm_norm_confirm = True
                            elif user_boolean.index(ii) == 1:
                                pl_norm_norm_confirm_no = True
                                print("Okay, versuchen wir das nochmal.")
                if not (pl_norm_norm_confirm_no or pl_norm_norm_confirm):
                    print(misunderstand[random.randint(0, len(misunderstand) - 1)])
                if pl_norm_norm_confirm_no:
                    break
        try:
            stage_2_pl_norm(Calc.Vector(pl_norm_sp_x, pl_norm_sp_y, pl_norm_sp_z),
                            Calc.Vector(pl_norm_norm_x, pl_norm_norm_y, pl_norm_norm_z))
            pl_norm_correct = True
        except SystemExit:
            print("Diese Vektoren beschreiben keine eindeutige Ebene.\nVersuchen wir das nochmal.")
    return [pl_norm_sp_x, pl_norm_sp_y, pl_norm_sp_z, pl_norm_norm_x, pl_norm_norm_y, pl_norm_norm_z]


def stage_2_def_pl_coord():
    print("Für die Ebenengleichung der Form: ax + by + cz = d")
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
                print("Diese Gleichung beschreibt keine Ebene.\nVersuchen wir das nochmal.")
                pl_coord_correct = False
            else:
                pl_coord_correct = True
        # confirm
        pl_coord_a_str = str(pl_coord_a)
        pl_coord_b_str = str(pl_coord_b)
        pl_coord_c_str = str(pl_coord_c)
        pl_coord_d_str = str(pl_coord_d)
        # a
        if pl_coord_a == 0:
            pl_coord_a_str = ""
        elif pl_coord_a < 0:
            pl_coord_b_str = "-" + str(abs(pl_coord_a)) + "x"
        elif pl_coord_a > 0:
            pl_coord_a_str = str(pl_coord_a) + "x"
        # b
        if pl_coord_b == 0:
            pl_coord_b_str = ""
        elif pl_coord_b < 0:
            if pl_coord_a == 0:
                pl_coord_b_str = "-" + str(abs(pl_coord_b)) + "y"
            else:
                pl_coord_b_str = " - " + str(abs(pl_coord_b)) + "y"
        elif pl_coord_b > 0:
            if pl_coord_a == 0:
                pl_coord_b_str = str(pl_coord_b) + "y"
            else:
                pl_coord_b_str = " + " + str(pl_coord_b) + "y"
        # c
        if pl_coord_c == 0:
            pl_coord_c_str = ""
        elif pl_coord_c < 0:
            if pl_coord_a == 0 and pl_coord_b == 0:
                pl_coord_c_str = "-" + str(abs(pl_coord_c)) + "z"
            else:
                pl_coord_c_str = " - " + str(abs(pl_coord_c)) + "z"
        elif pl_coord_c > 0:
            if pl_coord_a == 0 and pl_coord_b == 0:
                pl_coord_c_str = str(pl_coord_c) + "z"
            else:
                pl_coord_c_str = " + " + str(pl_coord_c) + "z"
        # d
        if pl_coord_d == 0:
            pl_coord_d_str = str(pl_coord_d)
        elif pl_coord_d < 0:
            pl_coord_d_str = str(pl_coord_d)
        elif pl_coord_d > 0:
            pl_coord_d_str = str(pl_coord_d)
        print("Also die Ebene:\n" + pl_coord_a_str + pl_coord_b_str +
              pl_coord_c_str + " = " + pl_coord_d_str + "?")
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
    return [pl_coord_a, pl_coord_b, pl_coord_c, pl_coord_d]


def stage_2_def_pl_pt():
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
        while not pl_pt_aa_confirm:
            pl_pt_aa_confirm_no = False
            pl_pt_aa_x_understand = False
            while not pl_pt_aa_x_understand:
                try:
                    pl_pt_aa_x = float(input("Wo ist dein erster Punkt(x-Koordinate): "))
                    pl_pt_aa_x_understand = True
                except ValueError:
                    print(misunderstand[random.randint(0, len(misunderstand) - 1)])
            pl_pt_aa_y_understand = False
            while not pl_pt_aa_y_understand:
                try:
                    pl_pt_aa_y = float(input("Wo ist dein erster Punkt(y-Koordinate): "))
                    pl_pt_aa_y_understand = True
                except ValueError:
                    print(misunderstand[random.randint(0, len(misunderstand) - 1)])
            pl_pt_aa_z_understand = False
            while not pl_pt_aa_z_understand:
                try:
                    pl_pt_aa_z = float(input("Wo ist dein erster Punkt(z-Koordinate): "))
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
        while not pl_pt_bb_confirm:
            pl_pt_bb_confirm_no = False
            pl_pt_bb_x_understand = False
            while not pl_pt_bb_x_understand:
                try:
                    pl_pt_bb_x = float(input("Wo ist dein zweiter Punkt(x-Koordinate): "))
                    pl_pt_bb_x_understand = True
                except ValueError:
                    print(misunderstand[random.randint(0, len(misunderstand) - 1)])
            pl_pt_bb_y_understand = False
            while not pl_pt_bb_y_understand:
                try:
                    pl_pt_bb_y = float(input("Wo ist dein zweiter Punkt(y-Koordinate): "))
                    pl_pt_bb_y_understand = True
                except ValueError:
                    print(misunderstand[random.randint(0, len(misunderstand) - 1)])
            pl_pt_bb_z_understand = False
            while not pl_pt_bb_z_understand:
                try:
                    pl_pt_bb_z = float(input("Wo ist dein zweiter Punkt(z-Koordinate): "))
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
        while not pl_pt_cc_confirm:
            pl_pt_cc_confirm_no = False
            pl_pt_cc_x_understand = False
            while not pl_pt_cc_x_understand:
                try:
                    pl_pt_cc_x = float(input("Wo ist dein dritter Punkt(x-Koordinate): "))
                    pl_pt_cc_x_understand = True
                except ValueError:
                    print(misunderstand[random.randint(0, len(misunderstand) - 1)])
            pl_pt_cc_y_understand = False
            while not pl_pt_cc_y_understand:
                try:
                    pl_pt_cc_y = float(input("Wo ist dein dritter Punkt(y-Koordinate): "))
                    pl_pt_cc_y_understand = True
                except ValueError:
                    print(misunderstand[random.randint(0, len(misunderstand) - 1)])
            pl_pt_cc_z_understand = False
            while not pl_pt_cc_z_understand:
                try:
                    pl_pt_cc_z = float(input("Wo ist dein dritter Punkt(z-Koordinate): "))
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
            stage_2_pl_pt(Calc.Point(pl_pt_aa_x, pl_pt_aa_y, pl_pt_aa_z),
                          Calc.Point(pl_pt_bb_x, pl_pt_bb_y, pl_pt_bb_z),
                          Calc.Point(pl_pt_cc_x, pl_pt_cc_y, pl_pt_cc_z))
            pl_pt_correct = True
        except SystemExit:
            print("Diese Punkte beschreiben keine eindeutige Ebene\nVersuchen wir das nochmal.")
    return [pl_pt_aa_x, pl_pt_aa_y, pl_pt_aa_z, pl_pt_bb_x, pl_pt_bb_y, pl_pt_bb_z, pl_pt_cc_x, pl_pt_cc_y, pl_pt_cc_z]


def obj_to_str(obj, rnd):  # Stage 5 Preparation
    output_str = ["-1"]
    if not (type(rnd) == float or type(rnd) == int):
        rnd = 2
    if type(obj) == int or type(obj) == float:
        obj_c = BasicMath.constant_round(obj, rnd)
        output_str.clear()
        output_str.append("Zahl " + str(obj_c))
    elif type(obj) == Calc.Point:
        pt_x = BasicMath.constant_round(obj.x, rnd)
        pt_y = BasicMath.constant_round(obj.y, rnd)
        pt_z = BasicMath.constant_round(obj.z, rnd)
        output_str.clear()
        output_str.append("Punkt (" + str(pt_x) + "|" + str(pt_y) + "|" + str(pt_z) + ")")
    elif type(obj) == Calc.Vector:
        vc_x = BasicMath.constant_round(obj.x, rnd)
        vc_y = BasicMath.constant_round(obj.y, rnd)
        vc_z = BasicMath.constant_round(obj.z, rnd)
        output_str.clear()
        output_str.append("Vektor (" + str(vc_x) + "|" + str(vc_y) + "|" + str(vc_z) + ")")
    elif type(obj) == Calc.Line:
        ln_sp_x = BasicMath.constant_round(obj.support.x, rnd)
        ln_sp_y = BasicMath.constant_round(obj.support.y, rnd)
        ln_sp_z = BasicMath.constant_round(obj.support.z, rnd)
        ln_dr_x = BasicMath.constant_round(obj.dr.x, rnd)
        ln_dr_y = BasicMath.constant_round(obj.dr.y, rnd)
        ln_dr_z = BasicMath.constant_round(obj.dr.z, rnd)
        output_str.clear()
        output_str.append("Gerade: x = (" + str(ln_sp_x) + "|" + str(ln_sp_y) + "|" + str(ln_sp_z) + ")"
                          " + (" + str(ln_dr_x) + "|" + str(ln_dr_y) + "|" + str(ln_dr_z) + ")s")
    elif type(obj) == Calc.Plane:
        pl_sp_x = BasicMath.constant_round(obj.support.x, rnd)
        pl_sp_y = BasicMath.constant_round(obj.support.y, rnd)
        pl_sp_z = BasicMath.constant_round(obj.support.z, rnd)
        pl_nm_x = BasicMath.constant_round(obj.normal.x, rnd)
        pl_nm_y = BasicMath.constant_round(obj.normal.y, rnd)
        pl_nm_z = BasicMath.constant_round(obj.normal.z, rnd)
        pl_dr1_x = BasicMath.constant_round(obj.dr1.x, rnd)
        pl_dr1_y = BasicMath.constant_round(obj.dr1.y, rnd)
        pl_dr1_z = BasicMath.constant_round(obj.dr1.z, rnd)
        pl_dr2_x = BasicMath.constant_round(obj.dr2.x, rnd)
        pl_dr2_y = BasicMath.constant_round(obj.dr2.y, rnd)
        pl_dr2_z = BasicMath.constant_round(obj.dr2.z, rnd)
        pl_a = BasicMath.constant_round(obj.a, rnd)
        pl_b = BasicMath.constant_round(obj.b, rnd)
        pl_c = BasicMath.constant_round(obj.c, rnd)
        pl_d = BasicMath.constant_round(obj.d, rnd)
        pl_a_str = str(pl_a)
        pl_b_str = str(pl_b)
        pl_c_str = str(pl_c)
        pl_d_str = str(pl_d)
        # a
        if pl_a == 0:
            pl_a_str = ""
        elif pl_a < 0:
            pl_b_str = "-" + str(abs(pl_a)) + "x"
        elif pl_a > 0:
            pl_a_str = str(pl_a) + "x"
        # b
        if pl_b == 0:
            pl_b_str = ""
        elif pl_b < 0:
            if pl_a == 0:
                pl_b_str = "-" + str(abs(pl_b)) + "y"
            else:
                pl_b_str = " - " + str(abs(pl_b)) + "y"
        elif pl_b > 0:
            if pl_a == 0:
                pl_b_str = str(pl_b) + "y"
            else:
                pl_b_str = " + " + str(pl_b) + "y"
        # c
        if pl_c == 0:
            pl_c_str = ""
        elif pl_c < 0:
            if pl_a == 0 and pl_b == 0:
                pl_c_str = "-" + str(abs(pl_c)) + "z"
            else:
                pl_c_str = " - " + str(abs(pl_c)) + "z"
        elif pl_c > 0:
            if pl_a == 0 and pl_b == 0:
                pl_c_str = str(pl_c) + "z"
            else:
                pl_c_str = " + " + str(pl_c) + "z"
        # d
        if pl_d == 0:
            pl_d_str = str(pl_d)
        elif pl_d < 0:
            pl_d_str = str(pl_d)
        elif pl_d > 0:
            pl_d_str = str(pl_d)
        output_str.clear()
        output_str.append("Ebene: x = (" + str(pl_sp_x) + "|" + str(pl_sp_y) + "|" + str(pl_sp_z) + ")"
                          " + (" + str(pl_dr1_x) + "|" + str(pl_dr1_y) + "|" + str(pl_dr1_z) + ")s"
                          " + (" + str(pl_dr2_x) + "|" + str(pl_dr2_y) + "|" + str(pl_dr2_z) + ")t")
        output_str.append("Ebene: 0 = (" + str(pl_nm_x) + "|" + str(pl_nm_y) + "|" + str(pl_nm_z) + ") * (x"
                          " - (" + str(pl_sp_x) + "|" + str(pl_sp_y) + "|" + str(pl_sp_z) + "))")
        output_str.append("Ebene: " + pl_a_str + pl_b_str + pl_c_str + " = " + pl_d_str)
    return output_str


def user_rnd():
    rnd_choice = 0
    rnd_understand = False
    print("Auf welche Nachkommastelle hättest du gerne deine Zahlen gerundet?")
    while not rnd_understand:
        rnd_understand = False
        try:
            rnd_choice = floor(float(input()))
            rnd_understand = True
            print("Okay gut.")
        except ValueError:
            print(misunderstand[random.randint(0, len(misunderstand) - 1)])
    return rnd_choice


def rnd_preference():
    rnd_prf = [0, False]
    rnd_confirm = False
    print("\nKurze Frage, hättest du gerne alle Zahlen gleich gerundet?")
    while not rnd_confirm:
        rnd_confirm_no = False
        user_vc_confirm = input().upper()
        for ii in user_boolean:
            for jj in ii:
                if user_vc_confirm == jj:
                    if user_boolean.index(ii) == 0:
                        rnd_confirm = True
                        print("Mhm.")
                        rnd_prf = [user_rnd(), True]
                    elif user_boolean.index(ii) == 1:
                        rnd_confirm_no = True
                        print("Okay verstanden.")
                        rnd_prf = [0, False]
        if not (rnd_confirm_no or rnd_confirm):
            print(misunderstand[random.randint(0, len(misunderstand) - 1)])
        if rnd_confirm_no:
            break
    return rnd_prf


# Task Object & Stage 2-6
class Task:
    def __init__(self, task_name, chosen_topic):
        self.task_name = task_name
        self.complete = False
        self.chosen_topic = chosen_topic
        self.obj_types = []
        self.obj_calc = []
        self.method_calc = [0.1, False]  # [index in topic / basic_method , if in basic_method]
        self.rnd = [2, False]
        self.sol = []  # Solution object
        self.solution = "-1 solution"  # Solution text

    # basic_define = Stage 2 & 3 for method == basic, else Stage 3(blank)
    def basic_define(self):  # Stage 3, return method as self.method_calc
        if self.chosen_topic != 3:
            self.method_calc.clear()
            self.method_calc.append(self.chosen_topic)
            self.method_calc.append(False)
        if self.chosen_topic == 3:
            # Stage 3
            self.method_calc.clear()
            print("\nOkay, zu " + self.task_name + ", da ging es um Grundrechnungen.\n"
                  "Um was genau ging es nochmal?")
            bm_type = 0.1
            bm_understand = False
            while not bm_understand:
                user_bm_answer = input().upper()
                for bm in basic_method:
                    for method_answer in bm:
                        if user_bm_answer == method_answer:
                            bm_understand = True
                            bm_type = basic_method.index(bm)
                if not bm_understand:
                    print(misunderstand[random.randint(0, len(misunderstand) - 1)])
            self.method_calc.append(bm_type)
            self.method_calc.append(True)
            # Stage 2
            if self.method_calc[1]:
                if self.method_calc[0] == 0:  # method plus
                    print("Ah, Addition von zwei Vektoren, warum auch nicht?\nDer erste Vektor, Vektor a:")
                    bm_plus_vc1 = stage_2_def_vc()
                    print("Okay gut, zum zweiten Vektor, Vektor b:")
                    bm_plus_vc2 = stage_2_def_vc()
                    self.obj_calc.append(stage_2_vc(bm_plus_vc1[0], bm_plus_vc1[1], bm_plus_vc1[2]))
                    self.obj_calc.append(stage_2_vc(bm_plus_vc2[0], bm_plus_vc2[1], bm_plus_vc2[2]))
                    print("Verstanden")
                elif self.method_calc[0] == 1:  # method minus
                    print("Also Subtraktion von zwei Vektoren, z.B. a - b? Gerne!\nDer erste Vektor, Vektor a:")
                    bm_minus_vc1 = stage_2_def_vc()
                    print("Verstehe, zum zweiten Vektor, Vektor b:")
                    bm_minus_vc2 = stage_2_def_vc()
                    self.obj_calc.append(stage_2_vc(bm_minus_vc1[0], bm_minus_vc1[1], bm_minus_vc1[2]))
                    self.obj_calc.append(stage_2_vc(bm_minus_vc2[0], bm_minus_vc2[1], bm_minus_vc2[2]))
                    print("Verstanden")
                elif self.method_calc[0] == 2:  # method scalar_multi
                    print("Skalarmultiplikation eines Vektors? Bin dabei!\n")
                    bm_scalar_multi_vc = stage_2_def_vc()
                    print("Okay gut.")
                    bm_scalar_multi_c = stage_2_def_c()
                    self.obj_calc.append(stage_2_vc(bm_scalar_multi_vc[0], bm_scalar_multi_vc[1],
                                                    bm_scalar_multi_vc[2]))
                    self.obj_calc.append(bm_scalar_multi_c)
                    print("Verstanden")
                elif self.method_calc[0] == 3:  # method scalar_product
                    print("Du brauchst das Skalarprodukt von zwei Vektoren? Bin dabei!\nDer erste Vektor, Vektor a:")
                    bm_scalar_product_vc1 = stage_2_def_vc()
                    print("Okay, zum zweiten Vektor, Vektor b:")
                    bm_scalar_product_vc2 = stage_2_def_vc()
                    self.obj_calc.append(stage_2_vc(bm_scalar_product_vc1[0], bm_scalar_product_vc1[1],
                                                    bm_scalar_product_vc1[2]))
                    self.obj_calc.append(stage_2_vc(bm_scalar_product_vc2[0], bm_scalar_product_vc2[1],
                                                    bm_scalar_product_vc2[2]))
                    print("Verstanden")
                elif self.method_calc[0] == 4:  # method vector_product
                    print("Aha, du brauchst das Kreuzprodukt von zwei Vektoren? Für dich doch gerne, " + username + ".")
                    print("Der erste Vektor, Vektor a:")
                    bm_vector_product_vc1 = stage_2_def_vc()
                    print("Gut, zum zweiten Vektor, Vektor b:")
                    bm_vector_product_vc2 = stage_2_def_vc()
                    self.obj_calc.append(stage_2_vc(bm_vector_product_vc1[0], bm_vector_product_vc1[1],
                                                    bm_vector_product_vc1[2]))
                    self.obj_calc.append(stage_2_vc(bm_vector_product_vc2[0], bm_vector_product_vc2[1],
                                                    bm_vector_product_vc2[2]))
                    print("Verstanden")
                elif self.method_calc[0] == 5:  # method spar_product
                    print("Oh, du brauchst das Spatprodukt von drei Vektoren? Für dich doch gerne, " + username + ".")
                    print("Also, der erste Vektor, Vektor a:")
                    bm_spar_product_vc1 = stage_2_def_vc()
                    print("Okay, zum zweiten Vektor, Vektor b:")
                    bm_spar_product_vc2 = stage_2_def_vc()
                    print("Verstehe, zum dritten Vektor, Vektor c:")
                    bm_spar_product_vc3 = stage_2_def_vc()
                    self.obj_calc.append(stage_2_vc(bm_spar_product_vc1[0], bm_spar_product_vc1[1],
                                                    bm_spar_product_vc1[2]))
                    self.obj_calc.append(stage_2_vc(bm_spar_product_vc2[0], bm_spar_product_vc2[1],
                                                    bm_spar_product_vc2[2]))
                    self.obj_calc.append(stage_2_vc(bm_spar_product_vc3[0], bm_spar_product_vc3[1],
                                                    bm_spar_product_vc3[2]))
                    print("Verstanden")
                elif self.method_calc[0] == 6:  # method unit
                    print("Ein bestimmter Einheitsvektor ist gesucht? Gerne doch!")
                    bm_unit_vc = stage_2_def_vc()
                    self.obj_calc.append(stage_2_vc(bm_unit_vc[0], bm_unit_vc[1], bm_unit_vc[2]))
                    print("Verstanden")
                elif self.method_calc[0] == 7:  # method ld
                    print("Ich wusste es! Du wolltest also zwischen zwei Vektoren nach linearer Abhängigkeit prüfen?"
                          " Schon dabei!\nZuerst Vektor a:")
                    bm_ld_vc1 = stage_2_def_vc()
                    print("Verstehe, zum zweiten Vektor, Vektor b:")
                    bm_ld_vc2 = stage_2_def_vc()
                    self.obj_calc.append(stage_2_vc(bm_ld_vc1[0], bm_ld_vc1[1], bm_ld_vc1[2]))
                    self.obj_calc.append(stage_2_vc(bm_ld_vc2[0], bm_ld_vc2[1], bm_ld_vc2[2]))
                    print("Verstanden")
                elif self.method_calc[0] == 8:  # method convert
                    print("Verstehe. Welches Objekt soll ich näher beschreiben?")
                    bm_conv_understand = False
                    bm_conv_obj_index = -1
                    while not bm_conv_understand:
                        bm_conv_input = input().upper()
                        for object_type_array in object_full_list:
                            for object_word in object_type_array:
                                if bm_conv_input == object_word:
                                    bm_conv_understand = True
                                    bm_conv_obj_index = object_full_list.index(object_type_array)
                        if not bm_conv_understand:
                            print(misunderstand[random.randint(0, len(misunderstand) - 1)] +
                                  "\nWelches Objekt soll ich für dich umrechnen?")
                    if bm_conv_obj_index == 0:
                        bm_conv_obj = stage_2_def_pt()
                        self.obj_calc.append(stage_2_pt(bm_conv_obj[0], bm_conv_obj[1], bm_conv_obj[2]))
                    elif bm_conv_obj_index == 1:
                        bm_conv_type = stage_2_line()
                        if bm_conv_type == 0:
                            bm_conv_obj = stage_2_def_ln_par()
                            self.obj_calc.append(stage_2_ln_par(Calc.Vector(bm_conv_obj[0],
                                                                            bm_conv_obj[1], bm_conv_obj[2]),
                                                                Calc.Vector(bm_conv_obj[3],
                                                                            bm_conv_obj[4], bm_conv_obj[5])))
                        elif bm_conv_type == 1:
                            bm_conv_obj = stage_2_def_ln_pt()
                            self.obj_calc.append(stage_2_ln_pt(Calc.Point(bm_conv_obj[0],
                                                                          bm_conv_obj[1], bm_conv_obj[2]),
                                                               Calc.Point(bm_conv_obj[3],
                                                                          bm_conv_obj[4], bm_conv_obj[5])))
                    elif bm_conv_obj_index == 2:
                        bm_conv_type = stage_2_plane()
                        if bm_conv_type == 0:
                            bm_conv_obj = stage_2_def_pl_par()
                            self.obj_calc.append(stage_2_pl_par(Calc.Vector(bm_conv_obj[0],
                                                                            bm_conv_obj[1], bm_conv_obj[2]),
                                                                Calc.Vector(bm_conv_obj[3],
                                                                            bm_conv_obj[4], bm_conv_obj[5]),
                                                                Calc.Vector(bm_conv_obj[6],
                                                                            bm_conv_obj[7], bm_conv_obj[8])))
                        elif bm_conv_type == 1:
                            bm_conv_obj = stage_2_def_pl_norm()
                            self.obj_calc.append(stage_2_pl_norm(Calc.Vector(bm_conv_obj[0],
                                                                             bm_conv_obj[1], bm_conv_obj[2]),
                                                                 Calc.Vector(bm_conv_obj[3],
                                                                             bm_conv_obj[4], bm_conv_obj[5])))
                        elif bm_conv_type == 2:
                            bm_conv_obj = stage_2_def_pl_coord()
                            self.obj_calc.append(stage_2_pl_coord(bm_conv_obj[0], bm_conv_obj[1],
                                                                  bm_conv_obj[2], bm_conv_obj[3]))
                        elif bm_conv_type == 3:
                            bm_conv_obj = stage_2_def_pl_pt()
                            self.obj_calc.append(stage_2_pl_pt(Calc.Point(bm_conv_obj[0],
                                                                          bm_conv_obj[1], bm_conv_obj[2]),
                                                               Calc.Point(bm_conv_obj[3],
                                                                          bm_conv_obj[4], bm_conv_obj[5]),
                                                               Calc.Point(bm_conv_obj[6],
                                                                          bm_conv_obj[7], bm_conv_obj[8])))
                    elif bm_conv_obj_index == 3:
                        bm_conv_obj = stage_2_def_vc()
                        self.obj_calc.append(stage_2_vc(bm_conv_obj[0], bm_conv_obj[1], bm_conv_obj[2]))

    # obj_define = Stage 2 for method != basic, else blank
    def obj_define(self):  # Stage 2
        if self.chosen_topic != 3:
            print("\nOkay, zu " + self.task_name + "(" + topic[self.chosen_topic][0] + " zwischen " +
                  object_full_list[self.obj_types[0]][0] + " und " + object_full_list[self.obj_types[1]][0] + "):")
            name_i = 1
            while name_i <= len(self.obj_types):
                print("\nDas " + str(name_i) + ". Objekt..")
                if self.obj_types[name_i - 1] == 0:
                    pt = stage_2_def_pt()
                    task_object = stage_2_pt(pt[0], pt[1], pt[2])
                    self.obj_calc.append(task_object)
                    print("Perfekt.")
                if self.obj_types[name_i - 1] == 1:
                    obj_ln_type = stage_2_line()
                    if obj_ln_type == 0:
                        print("Okay gut.")
                        ln = stage_2_def_ln_par()
                        self.obj_calc.append(stage_2_ln_par(Calc.Vector(ln[0], ln[1], ln[2]),
                                                            Calc.Vector(ln[3], ln[4], ln[5])))
                        print("Perfekt.")
                    if obj_ln_type == 1:
                        print("Verstanden.")
                        ln = stage_2_def_ln_pt()
                        self.obj_calc.append(stage_2_ln_pt(Calc.Point(ln[0], ln[1], ln[2]),
                                                           Calc.Point(ln[3], ln[4], ln[5])))
                        print("Perfekt.")
                if self.obj_types[name_i - 1] == 2:
                    obj_pl_type = stage_2_plane()
                    if obj_pl_type == 0:
                        print("Okay gut.")
                        pl = stage_2_def_pl_par()
                        self.obj_calc.append(stage_2_pl_par(Calc.Vector(pl[0], pl[1], pl[2]),
                                                            Calc.Vector(pl[3], pl[4], pl[5]),
                                                            Calc.Vector(pl[6], pl[7], pl[8])))
                        print("Perfekt.")
                    elif obj_pl_type == 1:
                        print("Verstanden.")
                        pl = stage_2_def_pl_norm()
                        self.obj_calc.append(stage_2_pl_norm(Calc.Vector(pl[0], pl[1], pl[2]),
                                                             Calc.Vector(pl[3], pl[4], pl[5])))
                        print("Perfekt.")
                    elif obj_pl_type == 2:
                        print("Okay gut.")
                        pl = stage_2_def_pl_coord()
                        self.obj_calc.append(stage_2_pl_coord(pl[0], pl[1], pl[2], pl[3]))
                        print("Perfekt.")
                    elif obj_pl_type == 3:
                        print("Verstehe.")
                        pl = stage_2_def_pl_pt()
                        self.obj_calc.append(stage_2_pl_pt(Calc.Point(pl[0], pl[1], pl[2]),
                                                           Calc.Point(pl[3], pl[4], pl[5]),
                                                           Calc.Point(pl[6], pl[7], pl[8])))
                        print("Perfekt.")
                if self.obj_types[name_i - 1] == 3:
                    vc = stage_2_def_vc()
                    task_object = stage_2_vc(vc[0], vc[1], vc[2])
                    self.obj_calc.append(task_object)
                    print("Perfekt.")
                name_i += 1

    # Stage 4
    def solve(self):  # sol == -1: error
        if self.method_calc[1]:
            sol_basic = -1
            if self.method_calc[0] == 0:  # Plus
                sol_basic = Calc.Basic.Vc.plus(self.obj_calc[0], self.obj_calc[1])
            elif self.method_calc[0] == 1:  # Minus
                sol_basic = Calc.Basic.Vc.minus(self.obj_calc[0], self.obj_calc[1])
            elif self.method_calc[0] == 2:  # scalar_multi
                sol_basic = Calc.Basic.Vc.smulti(self.obj_calc[0], self.obj_calc[1])
            elif self.method_calc[0] == 3:  # scalar_product
                sol_basic = Calc.Basic.Vc.sproduct(self.obj_calc[0], self.obj_calc[1])
            elif self.method_calc[0] == 4:  # vector_product
                sol_basic = Calc.Basic.Vc.vproduct(self.obj_calc[0], self.obj_calc[1])
            elif self.method_calc[0] == 5:  # spar_product
                sol_basic = Calc.Basic.Vc.sparproduct(self.obj_calc[0], self.obj_calc[1], self.obj_calc[2])
            elif self.method_calc[0] == 6:  # unit
                sol_basic = Calc.Basic.Vc.unit(self.obj_calc[0])
            elif self.method_calc[0] == 7:  # ld
                sol_basic = Calc.Basic.Vc.lindep(self.obj_calc[0], self.obj_calc[1])
            elif self.method_calc[0] == 8:  # convert
                sol_basic = self.obj_calc[0]
            self.sol.append(sol_basic)
        else:
            if self.method_calc[0] == 0:  # Distance
                sol_dis = -1
                if type(self.obj_calc[0]) == Calc.Point:
                    if type(self.obj_calc[1]) == Calc.Point:
                        sol_dis = Calc.Dis.point2(self.obj_calc[0], self.obj_calc[1])
                    elif type(self.obj_calc[1]) == Calc.Line:
                        sol_dis = Calc.Dis.pointline(self.obj_calc[0], self.obj_calc[1])
                    elif type(self.obj_calc[1]) == Calc.Plane:
                        sol_dis = Calc.Dis.pointplane(self.obj_calc[0], self.obj_calc[1])
                elif type(self.obj_calc[0]) == Calc.Line:
                    if type(self.obj_calc[1]) == Calc.Point:
                        sol_dis = Calc.Dis.pointline(self.obj_calc[0], self.obj_calc[1])
                    elif type(self.obj_calc[1]) == Calc.Line:
                        sol_dis = Calc.Dis.line2(self.obj_calc[0], self.obj_calc[1])
                    elif type(self.obj_calc[1]) == Calc.Plane:
                        sol_dis = Calc.Dis.lineplane(self.obj_calc[0], self.obj_calc[1])
                elif type(self.obj_calc[0]) == Calc.Plane:
                    if type(self.obj_calc[1]) == Calc.Point:
                        sol_dis = Calc.Dis.pointplane(self.obj_calc[0], self.obj_calc[1])
                    elif type(self.obj_calc[1]) == Calc.Line:
                        sol_dis = Calc.Dis.lineplane(self.obj_calc[0], self.obj_calc[1])
                    elif type(self.obj_calc[1]) == Calc.Plane:
                        sol_dis = Calc.Dis.plane2(self.obj_calc[0], self.obj_calc[1])
                self.sol.append(sol_dis)
            if self.method_calc[0] == 1:  # Cross
                sol_cross = -1
                if type(self.obj_calc[0]) == Calc.Line:
                    if type(self.obj_calc[1]) == Calc.Line:
                        try:
                            sol_cross = Calc.Cross.line2(self.obj_calc[0], self.obj_calc[1])
                        except SystemExit:
                            sol_cross = -1
                    elif type(self.obj_calc[1]) == Calc.Plane:
                        try:
                            sol_cross = Calc.Cross.lineplane(self.obj_calc[0], self.obj_calc[1])
                        except SystemExit:
                            sol_cross = -1
                elif type(self.obj_calc[0]) == Calc.Plane:
                    if type(self.obj_calc[1]) == Calc.Line:
                        try:
                            sol_cross = Calc.Cross.lineplane(self.obj_calc[0], self.obj_calc[1])
                        except SystemExit:
                            sol_cross = -1
                    elif type(self.obj_calc[1]) == Calc.Plane:
                        try:
                            sol_cross = Calc.Cross.plane2(self.obj_calc[0], self.obj_calc[1])
                        except SystemExit:
                            sol_cross = -1
                self.sol.append(sol_cross)
            if self.method_calc[0] == 2:  # Contain
                sol_con = -1
                # 0 = error, 1 = identical, 2 = parallel, 3 = cross point, 4 = skewed, 5 = outside
                if type(self.obj_calc[0]) == Calc.Point:
                    if type(self.obj_calc[1]) == Calc.Point:
                        sol_con = Calc.Con.point2(self.obj_calc[0], self.obj_calc[1])
                        if sol_con:
                            sol_con = 1
                        elif not sol_con:
                            sol_con = 5
                    elif type(self.obj_calc[1]) == Calc.Line:
                        sol_con = Calc.Con.pointline(self.obj_calc[0], self.obj_calc[1])
                        if sol_con:
                            sol_con = 1
                        elif not sol_con:
                            sol_con = 5
                    elif type(self.obj_calc[1]) == Calc.Plane:
                        sol_con = Calc.Con.pointplane(self.obj_calc[0], self.obj_calc[1])
                        if sol_con:
                            sol_con = 1
                        elif not sol_con:
                            sol_con = 5
                elif type(self.obj_calc[0]) == Calc.Line:
                    if type(self.obj_calc[1]) == Calc.Point:
                        sol_con = Calc.Con.pointline(self.obj_calc[0], self.obj_calc[1])
                        if sol_con:
                            sol_con = 1
                        elif not sol_con:
                            sol_con = 5
                    elif type(self.obj_calc[1]) == Calc.Line:
                        sol_con = Calc.Con.line2(self.obj_calc[0], self.obj_calc[1])
                    elif type(self.obj_calc[1]) == Calc.Plane:
                        sol_con = Calc.Con.lineplane(self.obj_calc[0], self.obj_calc[1])
                elif type(self.obj_calc[0]) == Calc.Plane:
                    if type(self.obj_calc[1]) == Calc.Point:
                        sol_con = Calc.Con.pointplane(self.obj_calc[0], self.obj_calc[1])
                        if sol_con:
                            sol_con = 1
                        elif not sol_con:
                            sol_con = 5
                    elif type(self.obj_calc[1]) == Calc.Line:
                        sol_con = Calc.Con.lineplane(self.obj_calc[0], self.obj_calc[1])
                    elif type(self.obj_calc[1]) == Calc.Plane:
                        sol_con = Calc.Con.plane2(self.obj_calc[0], self.obj_calc[1])
                self.sol.append(sol_con)

    # Stage 5 & 6
    def def_solution(self):
        sol_text = "-1"
        if not self.rnd[1]:
            self.rnd[0] = user_rnd()
        print("")
        if self.method_calc[1]:
            if self.method_calc[0] == 0:  # Plus
                sol_text = (self.task_name + " ist fertig.\nDas Ergebnis der Addition vom "
                            + obj_to_str(self.obj_calc[0], self.rnd[0])[0]
                            + " und vom " + obj_to_str(self.obj_calc[1], self.rnd[0])[0]
                            + " ist " + obj_to_str(self.sol[0], self.rnd[0])[0] + ".")
            elif self.method_calc[0] == 1:  # Minus
                sol_text = (self.task_name + " ist fertig. Das Ergebnis:\nDer "
                            + obj_to_str(self.obj_calc[0], self.rnd[0])[0]
                            + " minus dem" + obj_to_str(self.obj_calc[1], self.rnd[0])[0]
                            + " ist der " + obj_to_str(self.sol[0], self.rnd[0])[0] + ".")
            elif self.method_calc[0] == 2:  # scalar_multi
                sol_text = (self.task_name + " ist fertig. Das Ergebnis:\nDer "
                            + obj_to_str(self.obj_calc[0], self.rnd[0])[0]
                            + " mal der " + obj_to_str(self.obj_calc[1], self.rnd[0])[0]
                            + " ist der " + obj_to_str(self.sol[0], self.rnd[0])[0] + ".")
            elif self.method_calc[0] == 3:  # scalar_product
                sol_text = (self.task_name + " ist fertig. Das Ergebnis des Skalarproduktes:\nDer "
                            + obj_to_str(self.obj_calc[0], self.rnd[0])[0]
                            + " mal dem " + obj_to_str(self.obj_calc[1], self.rnd[0])[0]
                            + " ist die " + obj_to_str(self.sol[0], self.rnd[0])[0] + ".")
            elif self.method_calc[0] == 4:  # vector_product
                sol_text = (self.task_name + " ist fertig. Das Ergebnis des Kreuzproduktes:\nDer "
                            + obj_to_str(self.obj_calc[0], self.rnd[0])[0]
                            + " mal dem" + obj_to_str(self.obj_calc[1], self.rnd[0])[0]
                            + " ist der " + obj_to_str(self.sol[0], self.rnd[0])[0] + ".")
            elif self.method_calc[0] == 5:  # spar_product
                sol_text = (self.task_name + " ist fertig. Das Ergebnis:\nDas Spatprodukt vom "
                            + obj_to_str(self.obj_calc[0], self.rnd[0])[0]
                            + ", dem " + obj_to_str(self.obj_calc[1], self.rnd[0])[0]
                            + " und dem " + obj_to_str(self.obj_calc[2], self.rnd[0])[0]
                            + " ist " + str(BasicMath.constant_round(self.sol[0], self.rnd[0])) + ".")
            elif self.method_calc[0] == 6:  # unit
                sol_text = (self.task_name + " ist fertig.\nDer Einheitsvektor von dem "
                            + obj_to_str(self.obj_calc[0], self.rnd[0])[0]
                            + " ist der " + obj_to_str(self.sol[0], self.rnd[0])[0] + ".")
            elif self.method_calc[0] == 7:  # ld
                if self.sol[0]:
                    sol_text = (self.task_name + " ist fertig. Das Ergebnis:\nDer "
                                + obj_to_str(self.obj_calc[0], self.rnd[0])[0]
                                + " und der " + obj_to_str(self.obj_calc[1], self.rnd[0])[0]
                                + " sind linear abhängig.")
                else:
                    sol_text = (self.task_name + " ist fertig. Das Ergebnis:\nDer "
                                + obj_to_str(self.obj_calc[0], self.rnd[0])[0]
                                + " und der " + obj_to_str(self.obj_calc[1], self.rnd[0])[0]
                                + " sind linear unabhängig.")
            elif self.method_calc[0] == 8:  # convert
                if type(self.sol[0]) == Calc.Point:
                    sol_text = (self.task_name + " ist fertig. Hier ist dein Punkt:\n"
                                + obj_to_str(self.sol[0], self.rnd[0])[0] + ".\nDer ist "
                                + str(BasicMath.constant_round(self.sol[0].ov.l, self.rnd[0]))
                                + " Längeneinheiten vom Ursprung entfernt.")
                elif type(self.sol[0]) == Calc.Line:
                    sol_text = (self.task_name + " ist fertig. Hier ist deine Gerade:\n"
                                + obj_to_str(self.sol[0], self.rnd[0])[0] + ".")
                elif type(self.sol[0]) == Calc.Plane:
                    sol_text = (self.task_name + " ist fertig. Hier ist deine Ebene in Parameterform:\n"
                                + obj_to_str(self.sol[0], self.rnd[0])[0] + "."
                                + "\nUnd hier in der Normalenform:\n"
                                + obj_to_str(self.sol[0], self.rnd[0])[1] + "."
                                + "\nUnd hier in der Koordinatenform:\n"
                                + obj_to_str(self.sol[0], self.rnd[0])[2] + ".")
                elif type(self.sol[0]) == Calc.Vector:
                    sol_text = (self.task_name + " ist fertig. Hier ist dein Vektor:\n"
                                + obj_to_str(self.sol[0], self.rnd[0])[0] + ".\nDer ist "
                                + str(BasicMath.constant_round(self.sol[0].l, self.rnd[0]))
                                + " Längeneinheiten lang.\n")
        else:
            if self.method_calc[0] == 0:
                sol_text = (self.task_name + " ist fertig. Das Ergebnis:\nDer Abstand zwischen dem ersten Objekt,\n"
                            + obj_to_str(self.obj_calc[0], self.rnd[0])[0]
                            + ",\nund dem zweiten Objekt,\n" + obj_to_str(self.obj_calc[1], self.rnd[0])[0] + ","
                            + "\nsind " + str(BasicMath.constant_round(self.sol[0], self.rnd[0])) + " Längeneinheiten.")
            if self.method_calc[0] == 1:
                if self.sol[0] == -1:  # No Cross Area
                    sol_text = (self.task_name + " ist fertig. Das Ergebnis:\nZwischen dem ersten Objekt,\n"
                                + obj_to_str(self.obj_calc[0], self.rnd[0])[0]
                                + ",\nund dem zweiten Objekt,\n" + obj_to_str(self.obj_calc[1], self.rnd[0])[0]
                                + ",\nexistiert keine Schnittmenge.")
                else:  # Cross Area
                    sol_text = (self.task_name + " ist fertig. Das Ergebnis:\nZwischen dem ersten Objekt,\n"
                                + obj_to_str(self.obj_calc[0], self.rnd[0])[0]
                                + ",\nund dem zweiten Objekt,\n" + obj_to_str(self.obj_calc[1], self.rnd[0])[0]
                                + ",\nexistiert folgende Schnittmenge:\n"
                                + obj_to_str(self.sol[0], self.rnd[0])[0])
            if self.method_calc[0] == 2:
                if type(self.obj_calc[0]) == Calc.Point:
                    if type(self.obj_calc[1]) == Calc.Point:
                        if self.sol[0] == 1:
                            sol_text = (self.task_name + " ist fertig. Das Ergebnis:\nDer erste "
                                        + obj_to_str(self.obj_calc[0], self.rnd[0])[0]
                                        + " liegt im zweitem " + obj_to_str(self.obj_calc[1], self.rnd[0])[0] + ".")
                        if self.sol[0] == 5:
                            sol_text = (self.task_name + " ist fertig. Das Ergebnis:\nDer erste "
                                        + obj_to_str(self.obj_calc[0], self.rnd[0])[0]
                                        + " liegt nicht im zweitem "
                                        + obj_to_str(self.obj_calc[1], self.rnd[0])[0] + ".")
                    elif type(self.obj_calc[1]) == Calc.Line:
                        if self.sol[0] == 1:
                            sol_text = (self.task_name + " ist fertig. Das Ergebnis:\nDer "
                                        + obj_to_str(self.obj_calc[0], self.rnd[0])[0]
                                        + " liegt in der " + obj_to_str(self.obj_calc[1], self.rnd[0])[0] + ".")
                        if self.sol[0] == 5:
                            sol_text = (self.task_name + " ist fertig. Das Ergebnis:\nDer "
                                        + obj_to_str(self.obj_calc[0], self.rnd[0])[0]
                                        + " liegt nicht in der "
                                        + obj_to_str(self.obj_calc[1], self.rnd[0])[0] + ".")
                    elif type(self.obj_calc[1]) == Calc.Plane:
                        if self.sol[0] == 1:
                            sol_text = (self.task_name + " ist fertig. Das Ergebnis:\nDer "
                                        + obj_to_str(self.obj_calc[0], self.rnd[0])[0]
                                        + " liegt in der " + obj_to_str(self.obj_calc[1], self.rnd[0])[0] + ".")
                        if self.sol[0] == 5:
                            sol_text = (self.task_name + " ist fertig. Das Ergebnis:\nDer "
                                        + obj_to_str(self.obj_calc[0], self.rnd[0])[0]
                                        + " liegt nicht in der "
                                        + obj_to_str(self.obj_calc[1], self.rnd[0])[0] + ".")
                elif type(self.obj_calc[0]) == Calc.Line:
                    if type(self.obj_calc[1]) == Calc.Point:
                        if self.sol[0] == 1:
                            sol_text = (self.task_name + " ist fertig. Das Ergebnis:\nDer "
                                        + obj_to_str(self.obj_calc[1], self.rnd[0])[0]
                                        + " liegt in der " + obj_to_str(self.obj_calc[0], self.rnd[0])[0] + ".")
                        if self.sol[0] == 5:
                            sol_text = (self.task_name + " ist fertig. Das Ergebnis:\nDer "
                                        + obj_to_str(self.obj_calc[1], self.rnd[0])[0]
                                        + " liegt nicht in der "
                                        + obj_to_str(self.obj_calc[0], self.rnd[0])[0] + ".")
                    elif type(self.obj_calc[1]) == Calc.Line:
                        if self.sol[0] == 1:
                            sol_text = (self.task_name + " ist fertig. Das Ergebnis:\nDie erste "
                                        + obj_to_str(self.obj_calc[0], self.rnd[0])[0]
                                        + " liegt komplett innerhalb der zweiten "
                                        + obj_to_str(self.obj_calc[1], self.rnd[0])[0] + ".")
                        if self.sol[0] == 2:
                            sol_text = (self.task_name + " ist fertig. Das Ergebnis:\nDie erste "
                                        + obj_to_str(self.obj_calc[0], self.rnd[0])[0]
                                        + " ist parralel zur zweiten "
                                        + obj_to_str(self.obj_calc[1], self.rnd[0])[0] + ".")
                        if self.sol[0] == 3:
                            sol_text = (self.task_name + " ist fertig. Das Ergebnis:\nDie erste "
                                        + obj_to_str(self.obj_calc[0], self.rnd[0])[0]
                                        + " und die zweite "
                                        + obj_to_str(self.obj_calc[1], self.rnd[0])[0] + " schneiden sich.")
                        if self.sol[0] == 4:
                            sol_text = (self.task_name + " ist fertig. Das Ergebnis:\nDie erste "
                                        + obj_to_str(self.obj_calc[0], self.rnd[0])[0]
                                        + " ist zu der zweiten "
                                        + obj_to_str(self.obj_calc[1], self.rnd[0])[0] + " windschief.")
                    elif type(self.obj_calc[1]) == Calc.Plane:
                        if self.sol[0] == 1:
                            sol_text = (self.task_name + " ist fertig. Das Ergebnis:\nDie "
                                        + obj_to_str(self.obj_calc[0], self.rnd[0])[0]
                                        + " liegt komplett innerhalb der "
                                        + obj_to_str(self.obj_calc[1], self.rnd[0])[0] + ".")
                        if self.sol[0] == 2:
                            sol_text = (self.task_name + " ist fertig. Das Ergebnis:\nDie "
                                        + obj_to_str(self.obj_calc[0], self.rnd[0])[0]
                                        + " ist parralel zur "
                                        + obj_to_str(self.obj_calc[1], self.rnd[0])[0] + ".")
                        if self.sol[0] == 3:
                            sol_text = (self.task_name + " ist fertig. Das Ergebnis:\nDie "
                                        + obj_to_str(self.obj_calc[0], self.rnd[0])[0]
                                        + " schneidet die "
                                        + obj_to_str(self.obj_calc[1], self.rnd[0])[0] + ".")
                elif type(self.obj_calc[0]) == Calc.Plane:
                    if type(self.obj_calc[1]) == Calc.Point:
                        if self.sol[0] == 1:
                            sol_text = (self.task_name + " ist fertig. Das Ergebnis:\nDer "
                                        + obj_to_str(self.obj_calc[1], self.rnd[0])[0]
                                        + " liegt in der " + obj_to_str(self.obj_calc[0], self.rnd[0])[0] + ".")
                        if self.sol[0] == 5:
                            sol_text = (self.task_name + " ist fertig. Das Ergebnis:\nDer "
                                        + obj_to_str(self.obj_calc[1], self.rnd[0])[0]
                                        + " liegt nicht in der "
                                        + obj_to_str(self.obj_calc[0], self.rnd[0])[0] + ".")
                    elif type(self.obj_calc[1]) == Calc.Line:
                        if self.sol[0] == 1:
                            sol_text = (self.task_name + " ist fertig. Das Ergebnis:\nDie "
                                        + obj_to_str(self.obj_calc[1], self.rnd[0])[0]
                                        + " liegt komplett innerhalb der "
                                        + obj_to_str(self.obj_calc[0], self.rnd[0])[0] + ".")
                        if self.sol[0] == 2:
                            sol_text = (self.task_name + " ist fertig. Das Ergebnis:\nDie "
                                        + obj_to_str(self.obj_calc[1], self.rnd[0])[0]
                                        + " ist parralel zur "
                                        + obj_to_str(self.obj_calc[0], self.rnd[0])[0] + ".")
                        if self.sol[0] == 3:
                            sol_text = (self.task_name + " ist fertig. Das Ergebnis:\nDie "
                                        + obj_to_str(self.obj_calc[1], self.rnd[0])[0]
                                        + " schneidet die "
                                        + obj_to_str(self.obj_calc[0], self.rnd[0])[0] + ".")
                    elif type(self.obj_calc[1]) == Calc.Plane:
                        if self.sol[0] == 1:
                            sol_text = (self.task_name + " ist fertig. Das Ergebnis:\nDie erste "
                                        + obj_to_str(self.obj_calc[0], self.rnd[0])[0]
                                        + "\nliegt komplett innerhalb der zweiten "
                                        + obj_to_str(self.obj_calc[1], self.rnd[0])[0] + ".")
                        if self.sol[0] == 2:
                            sol_text = (self.task_name + " ist fertig. Das Ergebnis:\nDie erste "
                                        + obj_to_str(self.obj_calc[0], self.rnd[0])[0]
                                        + "\nist parralel zur zweiten "
                                        + obj_to_str(self.obj_calc[1], self.rnd[0])[0] + ".")
                        if self.sol[0] == 3:
                            sol_text = (self.task_name + " ist fertig. Das Ergebnis:\nDie erste "
                                        + obj_to_str(self.obj_calc[0], self.rnd[0])[0]
                                        + "\nund die zweite "
                                        + obj_to_str(self.obj_calc[1], self.rnd[0])[0] + " schneiden sich.")
        return sol_text

    # All Stages
    def get_solution(self):
        self.basic_define()
        self.obj_define()
        self.solve()
        self.solution = self.def_solution()
        self.complete = True


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
    if iteration == 1:
        user_topic = input("Zu was hast du denn deine Frage?\n").upper()
    else:
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
        chosen_task = Task(task_name, chosen_topic)
        chosen_task.obj_types.append(stage1[0])
        chosen_task.obj_types.append(stage1[1])
        task_list.append(chosen_task)
    elif chosen_topic == 1:
        stage1 = stage_1_cross()
        chosen_task = Task(task_name, chosen_topic)
        chosen_task.obj_types.append(stage1[0])
        chosen_task.obj_types.append(stage1[1])
        task_list.append(chosen_task)
    elif chosen_topic == 2:
        stage1 = stage_1_contain()
        chosen_task = Task(task_name, chosen_topic)
        chosen_task.obj_types.append(stage1[0])
        chosen_task.obj_types.append(stage1[1])
        task_list.append(chosen_task)
    elif chosen_topic == 3:
        print("Verstehe.")
        chosen_task = Task(task_name, chosen_topic)
        task_list.append(chosen_task)


# Chat
def early_game(iteration):
    iterate_understand = False
    iterate = 0
    while not iterate_understand:
        try:
            if iteration > 0:
                iterate = int(input("Wie viele weitere Fragen hast du für mich?\n"))
            else:
                iterate = int(input("Wie viele Fragen hast du für mich?\n"))
            iterate_understand = True
        except ValueError:
            print(misunderstand[random.randint(0, len(misunderstand) - 1)])

    for i in range(iterate):
        user_chosen_topic = stage_0(i + 1 + iteration)
        name = "Frage " + str(i + 1 + iteration)
        stage_1(user_chosen_topic, name)


def mid_game():
    rnd_main = rnd_preference()
    for aa in task_list:
        if not aa.complete:
            if rnd_main[1]:
                aa.rnd = rnd_main
            aa.get_solution()
            print(aa.solution)


def end_game():  # Stage 7
    print("")
    if len(task_list) in range(1, 8, 1):
        print("\nGut, alles ist fertig!")
    elif len(task_list) in range(9, 16, 1):
        print("\nSuper, habe alles fertig gerechnet!")
    elif len(task_list) in range(17, 24, 1):
        print("\nPuh, das war viel, aber wir haben es geschafft!")
    else:
        print("\nKrass, " + str(len(task_list)) + " Fragen! Aber wir haben es geschafft.")
    repeat_confirm = False
    while not repeat_confirm:
        repeat_confirm_no = False
        user_repeat = input("Hast du noch weitere Fragen?\n").upper()
        for ii in user_boolean:
            for jj in ii:
                if user_repeat == jj:
                    if user_boolean.index(ii) == 0:
                        repeat_confirm = True
                        print("Noch mehr Fragen? Schieß los!")
                        chat(len(task_list))
                    elif user_boolean.index(ii) == 1:
                        repeat_confirm_no = True
                        print("Okay super.")
                        print("Dann wohl bis später, " + username + ". Ich hoffe ich war hilfreich!")
        if not (repeat_confirm_no or repeat_confirm):
            print(misunderstand[random.randint(0, len(misunderstand) - 1)])
        if repeat_confirm_no:
            break


def chat(iteration):
    early_game(iteration)
    mid_game()
    end_game()


# Testing
chat(0)
