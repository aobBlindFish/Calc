import ChatMessage
import TimeFunction
import Humanize
import Chat_AnaGeo

# Key Var
no_answer = "Keine Antwort"
dummy = Humanize.Identity("Max", 0)
programmer = Humanize.Identity("Blind Fish", 0)

input_male = ["M", "MÄNNLICH", "MALE", "MANN", "JUNGE"]
input_female = ["W", "WEIBLICH", "FEMALE", "FRAU", "MÄDCHEN"]
input_sex = [input_male, input_female]
# Chat Start
print(ChatMessage.chat_enter_exit(programmer.name)[0])
print(ChatMessage.chat_msg(programmer.name,
                           "Hallo, ich bin " + programmer.name + ". "
                           "Damit die anderen und ich etwas mehr über dich wissen, "
                           "möchte ich dich eine kleine Umfrage ausfüllen lassen."))
TimeFunction.custom_delay(TimeFunction.med_delay)
print(ChatMessage.chat_msg(programmer.name,
                           'Falls du alle/bestimmte Fragen nicht beantworten möchtest, antworte stattdessen mit "'
                           + no_answer + '" oder auch ohne Text. Alle fehlenden Infos übernehmen wir von '
                           + dummy.name + ' Mustermann.'))
TimeFunction.custom_delay(TimeFunction.long_delay)
print("-- Umfrage --")
user_sex = dummy.sex
username = str(input("Benutzername: "))
if (username.upper() + " ").isspace() or username.upper() == no_answer.upper():
    username = dummy.name
user_sex_str = str(input("Geschlecht: "))
user_sex_understand = False
while not user_sex_understand:
    if (user_sex_str.upper() + " ").isspace() or user_sex_str.upper() == no_answer.upper():
        user_sex_understand = True
        user_sex = dummy.sex
    for ii in input_sex:
        for jj in ii:
            if user_sex_str.upper() == jj:
                user_sex_understand = True
                user_sex = input_sex.index(ii)
    if not user_sex_understand:
        user_sex_str = str(input("Was genau meinst du?\n"))
TimeFunction.custom_delay(TimeFunction.short_delay)
print(ChatMessage.chat_msg(programmer.name,
                           "Gut dankeschön, " + username + ". Ich hole mal die Hilfe für dich."))
TimeFunction.custom_delay(TimeFunction.short_delay)
print(ChatMessage.chat_enter_exit(programmer.name)[1])
Chat_AnaGeo.set_name(Humanize.Identity(username, user_sex), programmer)
# Chat Continue
Chat_AnaGeo.intro_game()
Chat_AnaGeo.chat(0)
