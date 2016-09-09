# -*- coding: utf-8 -*-
"""
Created on Thu Sep  1 08:42:03 2016

@author: Jarrett
"""

import math

test_impact = 30
test_balance = 5
test_survey = 15
test_online = test_impact + test_survey

def TimeCalc(subjects, volunteers):
   total_time = test_online + ((subjects * test_balance) * (1 / volunteers))
   return total_time


def VolCalc(subjects, time_avail):
    vol_needed = (subjects * test_balance) / (time_avail - test_online)
    return math.ceil(vol_needed)


def SubjCalc(volunteers, time_avail):
   subj_possible = (((time_avail - test_online) * volunteers)/ test_balance)
   return subj_possible

#Main Menu
print("Welcome to the CARE Consortium Baseline Testing Assistant")
print("Please choose what information you would like to know")
print("""1. How much time needed to complete testing
2. How many volunteers you need 
3. How many people you can test """)
answer = input("Your choice:")

if answer == "1":
    print("Section 1: Time to Complete Testing")
    subjects = int(input("How many subjects do you need to test? "))
    volunteers = int(input("How many volunteers do you have available? "))
    resultTimeCalc = TimeCalc(subjects, volunteers)
   if resultTimeCalc <= 60: 
      print("You need " + str(int(resultTimeCalc)) + " minutes for testing" )
   else:
      hours_need = int(resultTimeCalc / 60)
      extra_minutes = int(resultTimeCalc % 60)
      print("You need " + str(hours_need) + " hours and " + 
      str(extra_minutes) + " minutes")
    
elif answer == "2":
    print("Section 2: Number of Volunteers Needed")
    subjects = int(input("How many subjects do you need to test? "))
    time_avail = int(input("How much time do you have available in minutes? "))
    resultVolCalc = VolCalc(subjects, time_avail)
    print("You need " + str(int(resultVolCalc)) + " volunteers for testing")

elif answer == "3":
    print("Section 3: Number of Subjects to be Tested")
    volunteers = int(input("How many volunteers do you have available? "))
    time_avail = int(input("How much time do you have available in minutes? "))
    resultSubjCalc = SubjCalc(volunteers, time_avail)
    print("You can test " + str(int(resultSubjCalc)) + " students")

else:
    print("Please choose one of the proper sections")

