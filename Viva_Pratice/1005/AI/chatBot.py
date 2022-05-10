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
    "default": 
        "I didin't get that. Please try again"}


def res(mess):
    if(mess in resp):
        botRes = random.choice(resp[mess])
    else:
        botRes = resp["default"]    
    return botRes     
def send_message(mess):
    print(mess)
    response = res(mess)
    print(response)
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

print("Ask me Something")
while(1):
    inp = input()
    inp = inp.lower()
    relatedText = real(inp)
    send_message(relatedText)
    if inp == "exit" or inp == "stop":
        break