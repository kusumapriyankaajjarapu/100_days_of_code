"""
Given a string containing uppercase characters (A-Z), compress the string using Run Length encoding. Repetition of character has to be 
replaced by storing the length of that run.
Write a python function which performs the run length encoding for a given String and returns the run length encoded String.
"""


def encode(message):
    msg = ""
    count = 1
    l = len(message)
    if(l == 1):
        return "1" + message
    for i in range(0,l-1):
        if(message[i] == message[i+1]):
            count += 1
        else:
            msg += str(count) + message[i]
            count = 1
    if(message[l-2] != message[l-1]):
        msg += "1" + message[l-1]
    return msg


encoded_message=encode("ABBBBCCCCCCCCAB")
print(encoded_message)
