percent=float(input("Enter the percent of marks of student:"))
if percent>=90:
    grade='A'
elif percent>=80:
    grade='B'
elif percent>=70:
    grade='C'
elif percent>=60:
    grade='D'
elif percent>=50:
    grade='E'
else:
    grade='F'
print("Your Grade is:",grade)
