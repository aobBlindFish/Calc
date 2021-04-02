def chat_enter_exit(username):
    enter_str = "\n--- " + str(username) + " ist dem Chat beigetreten ---\n"
    exit_str = "\n--- " + str(username) + " hat den Chat verlassen ---\n"
    return [enter_str, exit_str]


def chat_msg(name, msg):
    output = ""
    if str(msg)[:1] == "\n":  # move linebreak to the front
        output += "\n" + str(name) + ": "
        for i in range(len(str(msg))-1):
            output += str(msg)[i + 1]
    else:
        output = str(name) + ": " + str(msg)
    return output


def chat_inv_kick(user1, user2):
    enter_str = "\n--- " + str(user1) + " hat " + str(user2) + " hinzugefügt ---\n"
    exit_str = "\n--- " + str(user1) + " hat " + str(user2) + " entfernt ---\n"
    return [enter_str, exit_str]


def str_trim(text, index_str):
    index = int(index_str)
    output = ""
    if float(index) < 0:
        for i in range(len(text) - abs(index)):
            output += text[i]

    elif float(index) > 0:
        for i in range(len(text) - index):
            output += text[i + index]

    else:
        output = text
    return output
