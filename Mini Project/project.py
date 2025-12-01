# count the number students
num_of_students = int(input("Enter Total Students: ")) 

# Data Store
student_lst = []
for i in range(num_of_students):
    print(i+1)
    name = input("Name: ")
    roll_num = int(input("Roll Number: "))
    Marks = int(input("Marks"))
    
    # Grades
    if(Marks>=95):
        grades = 'A+'
    elif Marks>=80 and Marks<95:
        grades = 'B+'
    elif Marks>=60 and Marks<80:
        grades = 'C'
    else:
        grades = 'D'
    
    Students_Data = {
        'Name': name,
        'Roll Number' : roll_num,
        'Marks' : Marks,
        'Grades' : grades
    }
    
    student_lst.append(Students_Data)


# # Data Print 
# for j in student_lst:
#     print(f"Name : {j['Name']}\nRoll Number : {j['Roll Number']}\nMarks : {j['Marks']}\nGrades : {j['Grades']}")

# students who are passed
for k in student_lst:
    if(k['Grades'] in ('A+','B+','C+')):
        print(f"PASS\nName : {k['Name']}\nRoll Number : {k['Roll Number']}\nMarks : {k['Marks']}\nGrades : {k['Grades']}")