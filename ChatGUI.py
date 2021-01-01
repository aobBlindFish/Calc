from math import *
import sys
import Calc

'''
Todo:
- Proper Machine Name
'''
'''
Stages:
0 == Introduction - Topic Asks
'''
# Meta Var
program_name = "Siri"
stage = 0

# Choice Arrays
topic_basic = ["BASISRECHNUNGEN", "GRUNDRECHNUNGEN", "GRUNDSACHEN"]
topic_dis = ["ABSTÄNDE", "ABSTAND"]
topic_cross = ["SCHNITTPUNKT", "SCHNITTPUNKTE", "SCHNITTGERADE", "SCHNITTGERADEN", "SCHNITTMENGE", "SCHNITTMENGEN"]
topic_contain = ["LAGEBEZIEHUNG", "LAGEBEZIEHUNGEN", "LAGEVERHÄLTNIS"]
topic = [topic_basic, topic_dis, topic_cross, topic_contain]


# Chat Start
print("Hallo, ich bin " + program_name + ". Wie heißt du?")
username = input()
print("Schön von dir zu hören, " + username + "!")
print("Du bist hier, um über Mathe zu reden? Freut mich!")
print("Von mir aus können wir gerne stundenlang über Schnittmengen, Abstände, Lagebeziehungen und weiteres sprechen!")
user_topic = input("Zu was hast du denn deine Frage?\n")
