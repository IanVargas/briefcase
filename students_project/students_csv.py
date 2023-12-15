import time,csv
from add_students import Student

headers = {
                    'Name',
                    'Class',
                    'Score_Spanish' , 
                    'Score_English' ,
                    'Score_Geography',
                    'Score_Science',
                    'Average'
}
def export_data_students_to_csv(students_dictionary_list):
 new_list_to_show_student_export = []
 for i in range (0,len(students_dictionary_list)):
    new_list_to_show_student_export.append(vars(students_dictionary_list[i]))

 try:
  with open ('Students data.csv','w', encoding="utf-8") as file:
    write_students_csv_files = csv.DictWriter(file,headers)
    write_students_csv_files.writeheader()
    write_students_csv_files.writerows(new_list_to_show_student_export)
    print("File created successfully")
    time.sleep(1)
   
 except IOError:
   print("unable to create file")
   time.sleep(1)
def import_data_csv_to_data(students_dictionary_list):
 imported_data = []
 try: 
   with open ('Students data.csv','r', encoding="utf-8") as file:
     count = 0
     read_file_csv = csv.DictReader(file)
     for row in read_file_csv:
      imported_data.append(row)
      print(imported_data)
      new_student = Student(imported_data[count]["Name"] , imported_data[count]["Class"], imported_data[count]["Score_Spanish"], imported_data[count]["Score_English"],
                              imported_data[count]["Score_Geography"],imported_data[count]["Score_Science"], imported_data[count]["Average"])
      students_dictionary_list.append(new_student)
      count =+ 1   
   return students_dictionary_list  
 except IOError:
   print("There's no file with that name")
   time.sleep(1)
   

