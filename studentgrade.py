
marks1 = float (input("Enter the marks for subject 1:"))
marks2 = float (input("Enter the marks for subject 2:"))
marks3 = float (input("Enter the marks for subject 3:"))
marks4 = float (input("Enter the marks for subject 4:"))
marks5 = float (input("Enter the marks for subject 5:"))

average = sum(marks1+marks2+marks3+marks4+marks5) / 5

if average >= 85:
    grade = 'A'
elif average >= 70:
    grade = 'B'
elif average >= 55:
    grade = 'C'
elif average >= 40:
    grade = 'D'
else:
    grade = 'Fail'


print(f"Average Marks: {average:.2f}")
print(f"Grade: {grade}")