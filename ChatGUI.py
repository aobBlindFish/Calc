import sys
import Calc
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
2 == Objects sent - Answer prepared
'''
# Meta Var
program_name = "Siri"
stage = 0
max_stage = 2

# Choice Arrays
topic_basic = ["BASISRECHNUNGEN", "GRUNDRECHNUNGEN", "GRUNDSACHEN"]
topic_dis = ["ABSTÄNDE", "ABSTAND"]
topic_cross = ["SCHNITTPUNKT", "SCHNITTPUNKTE", "SCHNITTGERADE", "SCHNITTGERADEN", "SCHNITTMENGE", "SCHNITTMENGEN"]
topic_contain = ["LAGEBEZIEHUNG", "LAGEBEZIEHUNGEN", "LAGEVERHÄLTNIS"]
topic = [topic_basic, topic_dis, topic_cross, topic_contain]

object_point = ["PUNKT"]
object_line = ["GERADE", "LINIE"]
object_plane = ["EBENE", "FLÄCHE", "OBERFLÄCHE"]
object_vector = ["VEKTOR", "RICHTUNG"]
object_full_list = [object_point, object_line, object_plane, object_vector]


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
                if user_dis_obj2.upper() == single_object and (object_list == object_line or object_list == object_plane):
                    user_object2_understand = True
                    chosen_object2 = object_full_list.index(object_list)
        if not user_object2_understand:
            print(misunderstand[random.randint(0, len(misunderstand)-1)])

    chosen_objects = [chosen_object1, chosen_object2]
    return chosen_objects


def stage_0():
    print("Du bist hier, um über Mathe zu reden? Freut mich!")
    print(
        "Von mir aus können wir gerne stundenlang über Schnittmengen, Abstände, Lagebeziehungen und weiteres sprechen!")
    user_topic = input("Zu was hast du denn deine Frage?\n").upper()
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
        return stage_1_dis()
    elif chosen_topic == 2:
        return stage_1_cross()


def stage_2(chosen_topic, object1, object2):
    if chosen_topic == 0:
        print("hi")
    elif chosen_topic == 1:
        print("hi")
    elif chosen_topic == 2:
        print("hi")
    return [chosen_topic, object1, object2]


# Chat Start
print("Hallo, ich bin " + program_name + ". Wie heißt du?")
username = input()
misunderstand = [username + ", ich weiß nicht genau, was du meinst.", "Was meinst du damit?", "Das verstehe ich nicht.",
                 "Das habe ich nicht verstanden."]
print("Schön von dir zu hören, " + username + "!")
user_chosen_topic = stage_0()
user_chosen_objects = stage_1(user_chosen_topic)
stage_2(user_chosen_topic, user_chosen_objects[0], user_chosen_objects[1])
