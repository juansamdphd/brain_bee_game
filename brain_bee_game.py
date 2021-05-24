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
import random

def main():
    # print welcoming message
    print("Welcome to Brainbeez! A text-based game to practice you neuroscience knowledge")
    # get user answer on what topic to review
    topic = get_user_topic()
    print("You've chosen", topic + ".\n" +  "To change topic, just type 'topic' as your answer to any of the questions.\nType 'exit' to leave.")
    print("")
    # print question from selected topic
    while True:
        question = ask_question(topic)
        if question == 'topic':
            print("")
            topic = get_user_topic()
            print("You've chosen", topic + ".\n" +  "To change topic, just type 'topic' as your answer to any of the questions.\nType 'exit' to leave.")
            print("")
        elif question == 'exit':
            break
    # print farewell message
    print("")
    print("Thanks for playing Brainbeez!\n")
    print("To learn more about the Brain Bee go to https://www.thebrainbee.org/\nor check your regional/local brain bee website.\n")
    print("Come back to practice some more any time you want\n")

def get_user_topic():
    topic = int(input("What do you want to practice or learn about today?\n1. History of Neuroscience\n2. Neuroanatomy\n3. Neurobiology\n4. Clinical neuroscience\n\nEnter your answer (just type the corresponding number or 0 to exit): "))
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
    with open("brainbeez_questions.txt") as file:
        question_bank = csv.DictReader(file, delimiter='\t')
        get_question = get_topic_question_list(question_bank, topic)
        question = input(get_question['question'] + " (hit enter to evaluate the answer): ")
        if question.lower() == get_question['answer'].lower():
            print("")
            print("Yes! This is the correct answer!\n")
        elif question.lower() == 'topic' or question.lower() == 'exit':
            return question
        else:
            print("")
            print("Incorrect answer. The answer is", get_question['answer'],"\n")

def get_topic_question_list(question_bank, topic):
    question_list = []
    for line in question_bank:
        if line['topic'] == topic:
            question_list.append(line)
    get_question = random.choice(question_list)
    return get_question

    
if __name__ == "__main__":
    main()