import StringPreset
import TimeFunction
import Humanize
import AnaGeo.Chat_AnaGeo

# Key Var
no_answer = "Keine Antwort"
help_word = "/help"
dummy = Humanize.Identity("Max", 0)
manager = Humanize.Identity("Chat Manager", 0)
programmer = Humanize.Identity("Blind Fish", 0)

input_male = ["M", "MÄNNLICH", "MALE", "MANN", "JUNGE"]
input_female = ["W", "WEIBLICH", "FEMALE", "FRAU", "MÄDCHEN"]
input_sex = [input_male, input_female]
# Chat Start
print(StringPreset.chat_enter_exit(manager.name)[0])
print(
    StringPreset.chat_msg(
        manager.name,
        "Hallo, ich bin " + manager.pronoun(4).lower() + " " + manager.name + ". "
        "Damit die anderen und ich etwas mehr über dich wissen, "
        "möchte ich dich eine kleine Umfrage ausfüllen lassen.",
    )
)
TimeFunction.custom_delay(TimeFunction.med_delay)
print(
    StringPreset.chat_msg(
        manager.name,
        'Falls du alle/bestimmte Fragen nicht beantworten möchtest, antworte stattdessen mit "'
        + no_answer
        + '" oder auch ohne Text. Alle fehlenden Infos übernehmen wir von '
        + dummy.name
        + " Mustermann.",
    )
)
TimeFunction.custom_delay(TimeFunction.long_delay)
print("-- Umfrage --")
user_sex = dummy.sex
username = str(input("Benutzername: "))
if (username.upper() + " ").isspace() or username.upper() == no_answer.upper():
    username = dummy.name
user_sex_str = str(input("Geschlecht: "))
user_sex_understand = False
while not user_sex_understand:
    if (
        user_sex_str.upper() + " "
    ).isspace() or user_sex_str.upper() == no_answer.upper():
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
print(
    StringPreset.chat_msg(
        manager.name,
        "Gut dankeschön, " + username + ". Ich hole mal die Hilfe für dich. "
        'Falls du mit etwas nicht klarkommst, sag einfach "' + help_word + '".',
    )
)
TimeFunction.custom_delay(TimeFunction.short_delay)
print(StringPreset.chat_enter_exit(manager.name)[1])
TimeFunction.custom_delay(2)
Chat_AnaGeo.set_data(Humanize.Identity(username, user_sex), programmer, help_word)
# Chat Continue
Chat_AnaGeo.intro_game()
Chat_AnaGeo.chat(0)
