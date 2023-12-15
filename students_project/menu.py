
import add_students,students_information,top_3_students,total_average_students,students_csv
import json , time, csv

def entry_point():
  students_dictionary_list = []  
  menu_items_actions(students_dictionary_list)
def menu_items_actions(students_dictionary_list) :

 i = int(input("""
               What do you want to do?
               1. Input new students information
               2. See Students information
               3. Top 3 students
               4. See your group avarage2
               5. Export your data to a csv
               6. Import your csv data 
               7. Exit  
                """))  
 if i == 1:
      students_dictionary_list = add_students.add_new_student_Data(students_dictionary_list)
      menu_items_actions(students_dictionary_list)

 elif i==2: 
     students_information.see_students_information(students_dictionary_list)
     menu_items_actions(students_dictionary_list)
 elif i==3:
     top_3_students.top_3_students(students_dictionary_list)
     menu_items_actions(students_dictionary_list)
 elif i==4:
     total_average_students.students_group_total_average(students_dictionary_list)
     menu_items_actions(students_dictionary_list)
 elif i==5:
     students_csv.export_data_students_to_csv(students_dictionary_list)
     menu_items_actions(students_dictionary_list)
 elif i==6:
     students_dictionary_list = students_csv.import_data_csv_to_data(students_dictionary_list)
     menu_items_actions(students_dictionary_list)
 elif i == 7 : 
      print("Thanks for choosing Us!")
      exit() 
 else:
      print("Not a valid option!")
      menu_items_actions(students_dictionary_list)  
entry_point()      