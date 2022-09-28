# Register Program
# The program will be used as a register for students to record their attendance
print("\t", "\t", "\t", "Register for student attendance".upper(), "\n")

student_ID_numbers = []
number_of_students = int(input("Enter the number of students that are registering : "))

for i in range(0, number_of_students):
    print("Enter the ID number of the student : ")
    ID_number = int(input())
    student_ID_numbers.append(ID_number)
print(student_ID_numbers)

with open("reg_form.txt", "w") as reg_form:
    reg_form.write(str(student_ID_numbers))
