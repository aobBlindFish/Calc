import sys
import Calc

'''
Todo:
- Proper Machine Name
- var completion
'''
'''
Stages:
0 == Introduction - Topic Asks
'''
# Meta Var
program_name = "Siri"
stage = 0
max_stage = 6

# Choice Arrays
topic_basic = ["BASISRECHNUNGEN", "GRUNDRECHNUNGEN", "GRUNDSACHEN"]
topic_dis = ["ABSTÄNDE", "ABSTAND"]
topic_cross = ["SCHNITTPUNKT", "SCHNITTPUNKTE", "SCHNITTGERADE", "SCHNITTGERADEN", "SCHNITTMENGE", "SCHNITTMENGEN"]
topic_contain = ["LAGEBEZIEHUNG", "LAGEBEZIEHUNGEN", "LAGEVERHÄLTNIS"]
topic = [topic_basic, topic_dis, topic_cross, topic_contain]


def stage_1_dis():
    print("hi")


def stage_0():
    print("Du bist hier, um über Mathe zu reden? Freut mich!")
    print(
        "Von mir aus können wir gerne stundenlang über Schnittmengen, Abstände, Lagebeziehungen und weiteres sprechen!")
    user_topic = input("Zu was hast du denn deine Frage?\n").upper()

    user_topic_understand = False
    for answer_list in topic:
        for answer in answer_list:
            if user_topic == answer:
                user_topic_understand = True
                chosen_topic = topic.index(answer_list)

    while not user_topic_understand:
        print("Ich weiß nicht was du meinst. Vielleicht weißt du auch nicht, was ich meine.")
        print("Ich kann dir gerne helfen, sobald es um Abstände, Schnittmengen, Lagebeziehungen oder allgemeine "
              "Grundsachen geht.")
        user_topic = input("In welchem Bereich brauchst du Hilfe?\n").upper()
        for answer_list in topic:
            for answer in answer_list:
                if user_topic == answer:
                    user_topic_understand = True
                    chosen_topic = topic.index(answer_list)
    return chosen_topic


def stage_1(chosen_topic):
    print("hi")


def story(lvl):
    if lvl == 0:
        stage_0()
    elif lvl == 1:
        stage_1()


# Chat Start
print("Hallo, ich bin " + program_name + ". Wie heißt du?")
username = input()
print("Schön von dir zu hören, " + username + "!")
stage_1(stage_0())
