#!/usr/bin/env python3
"""
file: pair_programming.py

Pair programming code for in-class activities.
Randomly assigns partners to tables and does the pair-programming timing.

author: M.P. Kuchera
date: 29 Jan 2018
edited: 14 Jan 2019
"""


import numpy as np
import time
import os
import sys

# global variables
students = ["Erik Adli", "Cathrine W. Tellefsen", "Haytham Ali", "Børge Irgens", \
            "Carol Norberg", "Tiago Pereira", "Ørjan Grøttem Martinsen", \
            "Tor Ole Odden", "Luiza Angheluta", "Daniela Gogova", "Lasse Clausen", \
            "Anja Røyne", "David André Coucheron", "Aksel Hiorth", "Olga Korostynska", \
            "Diana Quintero Castro", "Pål Andersen", "Einar Nathan", "Lisa Watson", \
            "Magnus Lilledahl" ]


# absent:   "" ,

def partner_assignments():
    print("There are", len(students), "students in the class. They are:")
    for student in students:
        print(student, end=",   ")

    students_per_group = 2

    num_groups = len(students) / students_per_group

    print("\n\nThere are",num_groups, "groups in the class.")

    np.random.shuffle(students)

    for i in range(0,int(num_groups)):
        print("\nTable ",i+1,": ",students[i*students_per_group],"and" ,students[i*students_per_group+1],end=" ")
      #  print(students[i*students_per_group],"and " ,students[i*students_per_group+1] )

    if(len(students)%students_per_group != 0):
        print("and" ,students[-1])

def coding_time():
    input("\n\nPress `Enter` when ready to start pair programming:")

    inp_min = input('How much time do the students have in minutes? ')
    minutes = float(inp_min)
    tot_time = minutes * 60
    inp_turn = input('How much time is one turn in minutes?')
    one_turn = float(inp_turn)*60
    print("\nStart coding!")
    os.system('say "Start Coding!"')

    for t in range(0,int(tot_time/one_turn)):
        time.sleep(one_turn)
        print("Time to switch roles!")
        sys.stdout.flush()
        os.system('say "Switch roles!"')

    time.sleep(one_turn)
    print("Time is up")
    sys.stdout.flush()
    os.system('say Time is up. ')


# main function
def main():
    # set partners and tables
    partner_assignments()
    #
    coding_time()

# run main() function iff we are executing THIS file.
#if __name__ == "__main__":
#    main()

    