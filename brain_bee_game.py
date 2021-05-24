"""
Brainbeez in Python:
Text-based game that presents neuroscience questions to
an user to practice and improve their neuroscience knowledge,
especially as the user prepares to a Brain Bee Competition

Author: Juan C. Sanchez-Arias. (https://www.github.com/juansamdphd/brain_bee_game/)
First version: 2021.
License; GPL.
"""

import csv

def main():
    # print welcoming message
    print("Welcome to Brainbeez! A text-based game to practice you neuroscience knowledge")
    # get user answer on what topic to review
    topic = get_user_topic()
    print("You've chosen", topic)
    # print question from selected topic
    questions = ask_question(topic)
    # print farewell message
    print("Thanks for playing Brainbeez!\n")
    print("To learn more about the Brain Bee go to https://www.thebrainbee.org/\nor check your regional/local brain bee website.\n")
    print("Come back to practice more any time you want")

def get_user_topic():
    topic = int(input("What do you want to practice or learn about today?\n1. History of Neuroscience\n2. Neuroanatomy\n3. Neurobiology\n4. Clinical neuroscience\nEnter your answer (just type the corresponding number or 0 to exit): "))
    while True:
        if topic > 4:
            topic = int(input("Invalid numner. Enter a valid number to select a topic or 0 to exit: "))
        if topic == 1:
            # get a history question
            topic = "history"
            return topic
        elif topic == 2:
            # get a neuroanatomy question
            topic = "neuroanatomy"
            return topic
        elif topic == 3:
            # get a neurobiology question
            topic = "neurobiology"
            return topic
        elif topic == 4:
            # get a clinical question
            topic = "clinical"
            return topic
        elif topic == 0:
            topic = "to exit"
            return topic

def ask_question(topic):
    with open("brainbeez_questions.csv") as file:
        questions = csv.DictReader(file)
        for line in questions:
            if line['topic'] == topic:
                print(line['question'])


    
if __name__ == "__main__":
    main()