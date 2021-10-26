#This program stores the inputted names in an array and counts the stored values, when the user inputs the word 'stop' the program will display all the values stored in the array

#array to store the users inputs
student_names_array=[]


#repetition structure
while True:
  next_student = str(input("Next student:")).lower()
  if(next_student == "stop" or next_student == "STOP"):
    break
  else:
    student_names_array.append(next_student)

print ("You have entered all the names of the students in your class")
    
print(student_names_array)

print("Your list consists of" + " " + str(len(student_names_array)) + " " + "students")
