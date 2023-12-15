import time

def top_3_students(students_dictionary_list):
   
   if students_dictionary_list:
    sorted_students = sorted(students_dictionary_list, key=lambda students_dictionary_list: students_dictionary_list.Average, reverse=True)

    for index in range(0, 3):
      if index < len(sorted_students):
        student = sorted_students[index]
        print(f'The Top {index + 1} student is {student.Name} with score {student.Average}')

    time.sleep(1)

   
   else: 
    print("There's no data to show") 
    time.sleep(1)