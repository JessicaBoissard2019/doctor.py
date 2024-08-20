"""
Program: doctor.py
Jessica Boissard
8/2/2024
Application that simulates an interactive session of nondirective psychotherapy.
"""

import random

#Global variables of various lists of data that all functions can share

hedges = ("Please, tell me more.", "Many of my patients tell me the same thing.", "Please, continue.", "Go on, go on...", "You dont say...")

qualifiers = ("Why do you say that ", "You seem to think that ", "Can you explain why ")

replacements = {"I":"you", "me":"you", "my":"your", "we":"you", "us":"you", "am":"are", "you":"I"}

#definition of th ereply() function
def reply(sentence):
    """ Builds and returns a reply to the user input"""
    probability = random.randint(1, 4)
    if probability ==1:
        return random.choice(hedges)
    else:
        return random.choice(qualifiers) + changePerson(sentence)
#Definition of the changePerson() function
def changePerson(sentence):
    """ Replaces first-person pronouns with second-person pronouns."""
    words = sentence.split()
    replyWords = []
    for word in words:
        replyWords.append(replacements.get(word, word))
    return" ".join(replyWords)

#Definition of the main()function
def main():
    """ Handles the interaction between user and doctor"""
    print("Good day, I hope you are well today.")
    print("what can I do for you?")
    while True:
        sentence = input("\nType your response or QUIT to exit >> ")
        if sentence.upper() == "QUIT":
            input("Have a great day! Press ENTER to exit program >> ")
            break
        print(reply(sentence))
#Global call to main() for program execution
if __name__=='__main__':    
    main()