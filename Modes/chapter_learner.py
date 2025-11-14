import sqlite3
import random
import os
import time
import sys

## Convert Database to something workable
def extract(chapter):
    for n in range(0, len(collected)):
        extracted.append([collected[n][1], collected[n][2]])

## Questioner Russian to
def question(index):
    if index == 0:
        correct = 1
    else:
        correct = 0

    total_iterations = 100
    goal = 0
    failure = 0

    while goal != 10 and failure != 10:
        rando = random.randint(0, len(extracted)-1)

        progress_bar(goal * 10, total_iterations, prefix='Punkte:', suffix='Win', length=50)
        failure_bar(failure * 10, total_iterations, prefix='Fehler:', suffix='Game Over', length=50)

        vocabular = input("Was ist die Übersetzung von \"" + extracted[rando][index] + "\" : ")
        

        if vocabular.lower() == extracted[rando][correct].lower():
            print("Richtig! Die Übersetzung von \"" + extracted[rando][index] + "\" lautet: \"" + extracted[rando][correct] + "\"")
            time.sleep(3)
            os.system('clear')
            goal += 1
        else:
            print("Leider falsch! Die Übersetzung von \"" + extracted[rando][index] + "\" lautet: \"" + extracted[rando][correct] + "\"")
            time.sleep(3)
            os.system('clear')
            failure += 1
    os.system('clear')
    if goal == 10:
        print("Glückwunsch, du hast das Kapitel " + chapter + " gemeistert!")
    else:
        print("Leider hast du das Kapitel " + chapter + " nicht geschafft. Gib nicht auf!")

## Goal Bar 
def progress_bar(iteration, total, prefix='', suffix='', decimals=1, length=100, fill='█'):
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filled_length = int(length * iteration // total)
    bar = fill * filled_length + '-' * (length - filled_length)
    sys.stdout.write(f'\r{prefix} |{bar}| {percent}% {suffix}')
    sys.stdout.flush()
    

## Failure Bar
def failure_bar(iteration, total, prefix='', suffix='', decimals=1, length=100, fill='█'):
    print("")
    print("")
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filled_length = int(length * iteration // total)
    bar = fill * filled_length + '-' * (length - filled_length)
    sys.stdout.write(f'\r{prefix} |{bar}| {percent}% {suffix}')
    sys.stdout.flush()
    for n in range(5):
        print("") 
     

## Backend
os.system('clear')
conn = sqlite3.connect("vocabulary.db")
cur = conn.cursor()
chapter = input("Здравствуй, welches Kapitel möchtes du lernen? : ")
index = int(input("Wie möchtest du lernen? [0] Russisch - Deutsch [1] Deutsch - Russisch : "))
database = cur.execute('select * from vocabs where chapter = ?', (chapter,))
collected = cur.fetchall()

## Main
extracted = []
os.system('clear')
extract(chapter)
question(index)