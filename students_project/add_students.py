

import json , time, csv

range_for_scores = range(0,100+1) 

class Student : 
  Name : str
  Class : str
  Score_Spanish : int
  Score_English : int
  Score_Geography : int
  Score_Science : int
  Average : int
  def __init__(self,Name,Class, Score_Spanish , Score_English , Score_Geography, Score_Science, Average): 
     self.Name = Name
     self.Class = Class
     self.Score_Spanish = Score_Spanish
     self.Score_English = Score_English
     self.Score_Geography = Score_Geography
     self.Score_Science = Score_Science
     self.Average = Average


def add_new_student_Data(students_dictionary_list):
  amount_of_students = amount_of_students_to_input()
  if amount_of_students == 0:
    return
  else:  
   for i in range (0,amount_of_students):
    student_full_name = input("What's the student name?")
    student_class = input("What's the student class?")
    student_score_spanish = student_score_spanish_input()
    student_score_english = student_score_english_input()
    student_score_geography = student_score_geography_input()
    student_score_science = student_score_science_input()
    average_notes_students = ((student_score_english+student_score_science+student_score_geography+student_score_spanish) / 4)
    new_student = Student(student_full_name,student_class , student_score_spanish, student_score_english,student_score_geography,student_score_science, average_notes_students)
    students_dictionary_list.append(new_student)
   return students_dictionary_list
  
def amount_of_students_to_input():
  amount_of_students = -1
  continue_to_next_phase = True
  while  continue_to_next_phase :
       try:
        amount_of_students = int(input("How much students do you want to add?"))
       except ValueError:
        print("Wrong Input!! please input a whole number")
       if amount_of_students <= -1:
         print ("You can't add negative students")
       elif amount_of_students == 0:
         print("No Student's will be add to the list!!!, Thanks")
         continue_to_next_phase = False  
         time.sleep(1) 
       else: 
         continue_to_next_phase = False  
  return amount_of_students 
    
def student_score_spanish_input():
  student_score_spanish = 200
  while  student_score_spanish not in range_for_scores:
       try:
        student_score_spanish = float(input("What's the student score in spanish?"))
       except ValueError:
        print("You can just add numbers to this value, not letters.")
       if student_score_spanish not in range_for_scores:
        print("Input a score between 0 and 100")
  return student_score_spanish 

def student_score_english_input():
 student_score_english = 200
 while  student_score_english not in range_for_scores:
       try:
        student_score_english = float(input("What's the student score in English?"))
       except ValueError:
        print("You can just add numbers to this value, not letters.")
       if student_score_english not in range_for_scores:
        print("Input a score between 0 and 100")
 return student_score_english 

def student_score_geography_input():
    
 student_score_geography = 200
 while  student_score_geography not in range_for_scores:
       try:
        student_score_geography = float(input("What's the student score in Geography?"))
       except ValueError:
        print("You can just add numbers to this value, not letters.")
       if student_score_geography not in range_for_scores:
        print("Input a score between 0 and 100")
 return student_score_geography 

def student_score_science_input():
 student_score_science = 200
 while  student_score_science not in range (0,100+1):
       try: 
        student_score_science = float(input("What's the student score in science?"))
       except ValueError: 
        print("You can just add numbers to this value, not letters.")
       if student_score_science not in range (0,100+1):
        print("Input a score between 0 and 100")
 return student_score_science 
