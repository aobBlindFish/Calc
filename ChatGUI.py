import sys
import Calc
from math import *
import random

'''
Todo:
- Proper Machine Name
- var completion
'''
'''
Stages:
0 == Introduction - Topic chosen
1 == Objects asked - Objects chosen
2 == Chosen objects defined as Calc.py-objects
3 == Solution calculated
4 == Calc.py-solution defined into words
5 == Solution returned
6 == Repeat or End
'''
# Meta Var
program_name = "Siri"
stage = 0
max_stage = 2

# Choice Arrays
task_list = []

topic_basic = ["BASISRECHNUNGEN", "GRUNDRECHNUNGEN", "GRUNDSACHEN"]
topic_dis = ["ABSTÄNDE", "ABSTAND", "DISTANZ", "DISTANZEN", "ENTFERNUNG", "ENTFERNUNGEN"]
topic_cross = ["SCHNITTPUNKT", "SCHNITTPUNKTE", "SCHNITTGERADE", "SCHNITTGERADEN", "SCHNITTMENGE", "SCHNITTMENGEN"]
topic_contain = ["LAGEBEZIEHUNG", "LAGEBEZIEHUNGEN", "LAGEVERHÄLTNIS", "LAGE"]
topic = [topic_basic, topic_dis, topic_cross, topic_contain]

object_point = ["PUNKT"]
object_line = ["GERADE", "LINIE"]
object_plane = ["EBENE", "FLÄCHE", "OBERFLÄCHE"]
object_vector = ["VEKTOR", "RICHTUNG"]
object_full_list = [object_point, object_line, object_plane, object_vector]


# Task Object
class Task:
    def __init__(self, chosen_method, obj_type1, obj_type2):
        self.complete = False
        self.chosen_method = chosen_method
        self.obj_type1 = obj_type1
        self.obj_type2 = obj_type2


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
            print(misunderstand[random.randint(0, len(misunderstand)-1)])

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
            print(misunderstand[random.randint(0, len(misunderstand)-1)])

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
            print(misunderstand[random.randint(0, len(misunderstand)-1)])

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
            print(misunderstand[random.randint(0, len(misunderstand)-1)])

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
            print(misunderstand[random.randint(0, len(misunderstand)-1)])

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
            print(misunderstand[random.randint(0, len(misunderstand)-1)])

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


def stage_1(chosen_topic):
    if chosen_topic == 0:
        print("hi")
    elif chosen_topic == 1:
        stage1 = stage_1_dis()
        chosen_task = Task(chosen_topic, stage1[0], stage1[1])
        task_list.append(chosen_task)
    elif chosen_topic == 2:
        stage1 = stage_1_cross()
        chosen_task = Task(chosen_topic, stage1[0], stage1[1])
        task_list.append(chosen_task)
    elif chosen_topic == 3:
        stage1 = stage_1_contain()
        chosen_task = Task(chosen_topic, stage1[0], stage1[1])
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
    user_chosen_topic = stage_0(i+1)
    stage_1(user_chosen_topic)
print(task_list)
