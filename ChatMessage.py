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
