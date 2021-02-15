def chat_enter_exit(username):
    enter_str = "\n--- " + str(username) + " ist dem Chat betreten ---\n"
    exit_str = "\n--- " + str(username) + " hat den Chat verlassen ---\n"
    return [enter_str, exit_str]


def chat_msg(username, msg):
    return str(username) + ": " + str(msg)


def chat_inv_kick(user1, user2):
    enter_str = "\n--- " + str(user1) + " hat " + str(user2) + " hinzugefügt ---\n"
    exit_str = "\n--- " + str(user1) + " hat " + str(user2) + " entfernt ---\n"
    return [enter_str, exit_str]
