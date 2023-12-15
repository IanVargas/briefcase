
import json , time, csv
from tabulate import tabulate

def see_students_information(students_dictionary_list):
  new_list_to_show_student = []
  for i in range (0,len(students_dictionary_list)):
    new_list_to_show_student.append(vars(students_dictionary_list[i]))

  if students_dictionary_list:
    print(tabulate(new_list_to_show_student, headers="keys", tablefmt="pretty"))
  else:
    print("There's no data on the file") 
  time.sleep(1)
   