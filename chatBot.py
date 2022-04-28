import random
name = "Bot Number 286"
monsoon = "rainy"
mood = "Smiley"
resp = {
    "what's your name?": [
        "They call me {0}".format(name),
        "I usually go by {0}".format(name),
        "My name is the {0}".format(name)],
    "what's today's weather?": [
        "The weather is {0}".format(monsoon),
        "It's {0} today".format(monsoon)],
    "how are you?": [
        "I am feeling {0}".format(mood),
        "{0}! How about you?".format(mood),
        "I am {0}! How about yourself?".format(mood), ],
    # "": [
    #     "What do you mean by these?",
    # ],
    "default": [
        "I didin't get that. Please try again"]}


def res(message):
    if message in resp:
        bot286_message = random.choice(resp[message])
    else:
        bot286_message = random.choice(resp["default"])
    return bot286_message


def real(xtext):
    if "name" in xtext:
        ytext = "what's your name?"
    elif "weather" in xtext:
        ytext = "what's today's weather?"
    elif "how are" in xtext:
        ytext = "how are you?"
    else:
        ytext = ""
    return ytext


def send_message(message):
    print((message))
    response = res(message)
    print((response))

print("Ask me something")
while 1:
    
    my_input = input()
    my_input = my_input.lower()
    related_text = real(my_input)
    send_message(related_text)
    if my_input == "exit" or my_input == "stop":
        break
