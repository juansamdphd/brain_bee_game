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
    print("Welcome to Brainbeez! A text-based game to practice your neuroscience knowledge")
    # get user answer on what topic to review
    topic = get_user_topic()
    print("You've chosen", topic + ".\n" +  "To change topic, just type 'topic' as your answer to any of the questions.\nType 'exit' to leave.")
    print("")
    # print question from selected topic
    question_list = get_questions(topic)
    while question_list:
        question = ask_question(question_list)
        if question == 'topic':
            print("")
            topic = get_user_topic()
            print("You've chosen", topic + ".\n" +  "To change topic, just type 'topic' as your answer to any of the questions.\nType 'exit' to leave.")
            print("")
        elif question == 'exit':
            break
        elif not question_list:
            print("That's all we have! Make sure to check us out again for more content.\nWe will be expanding our the program function and question bank")
    # print farewell message
    print("")
    print("Thanks for playing Brainbeez!\n")
    print("To learn more about the Brain Bee go to https://www.thebrainbee.org/\nor check your regional/local brain bee website.\n")
    print("Come back to practice some more any time you want\n")

def get_user_topic():
    # gets user topic to practice
    topic = int(input("What do you want to practice or learn about today?\n1. History of Neuroscience\n2. Neuroanatomy\n3. Neurobiology\n4. Clinical neuroscience\n\nEnter your answer (just type the corresponding number or 0 to exit): "))
    while True: # as topics get added this value can change
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

def get_questions(topic):
    # opens text file with questions from a tab delimited file
    with open("brainbeez_questions.txt") as file:
        question_bank = csv.DictReader(file, delimiter='\t') # uses csv.DictReader to make first line as headers and defines the delimiter as tab
        # Get list of questions
        question_list = get_topic_question_list(question_bank, topic)
        # Get a question from question list
        # question = get_question(question_list)
    return question_list
        # while question_list:
        #     question = question_list.pop(random.randrange(len(question_list)))

def get_topic_question_list(question_bank, topic):
    question_list = [] # creates an empty to append available quesitons which topic matches the one selected by the user.
    for line in question_bank:
        if line['topic'] == topic:
            question_list.append(line) # appends questions to list
    return question_list

def ask_question(question_list):
    # sample_list = random.sample(question_list, len(question_list)) # from the random library gets a random item from question_list
    question = question_list.pop(random.randrange(len(question_list)))
    # return question
    # Ask question to user and record answer
    user_answer = input(question['question'] + " (hit enter to evaluate the answer): ")
    # Compare user_answer with question answer
    if user_answer.lower() == question['answer'].lower(): # compared as lower in case there is mix of upper and lower case
        print("")
        print("Yes! This is the correct answer!\n")
    elif user_answer.lower() == 'topic' or user_answer.lower() == 'exit': # adds option to exit or change topic of practice
        return user_answer
    else:
        print("")
        print("Incorrect answer. The answer is", question['answer'],"\n")
    
if __name__ == "__main__":
    main()