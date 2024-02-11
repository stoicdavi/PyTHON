# A program to calculate the average marks of a student and display the grade.
marks1 = int(input("Enter marks for subject 1: "))
marks2 = int(input("Enter marks for subject 2: "))
marks3 = int(input("Enter marks for subject 3: "))
average = (marks1 + marks2 + marks3) / 3
if average >= 90:
    grade = "A"
elif average >= 70 and average < 90:
    grade = "B"
elif average >= 50 and average < 70:
    grade = "C"
elif average > 39 and average < 50:
    grade = "D"
else:
    grade = "F"
print("Your average marks are {} and your grade is {}".format(average, grade))