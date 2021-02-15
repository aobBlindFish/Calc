def chat_enter_exit(username):
    enter_str = "--- " + str(username) + " ist dem Chat betreten ---"
    exit_str = "--- " + str(username) + " hat den Chat verlassen ---"
    return [enter_str, exit_str]


def chat_msg(username, msg):
    return str(username) + ": " + str(msg)


def chat_inv_kick(user1, user2):
    enter_str = "--- " + str(user1) + " hat " + str(user2) + " hinzugefügt ---"
    exit_str = "--- " + str(user1) + " hat " + str(user2) + " entfernt ---"
    return [enter_str, exit_str]
