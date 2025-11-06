print("Welcome to GradeBook Analyzer!\n")

n = int(input("How many students? "))

students = {}
for i in range(n):
    name = input(f"Enter name of student {i+1}: ")
    marks = float(input(f"Enter marks for {name}: "))
    students[name] = marks

grades = {}
for name, marks in students.items():
    if marks >= 90:
        grade = 'A'
    elif marks >= 80:
        grade = 'B'
    elif marks >= 70:
        grade = 'C'
    elif marks >= 60:
        grade = 'D'
    else:
        grade = 'F'
    grades[name] = grade

all_marks = list(students.values())
average = sum(all_marks) / len(all_marks)
highest = max(all_marks)
lowest = min(all_marks)

passed = [name for name, m in students.items() if m >= 40]
failed = [name for name, m in students.items() if m < 40]

print("\nName\tMarks\tGrade")
print("-----------------------")
for name in students:
    print(f"{name}\t{students[name]}\t{grades[name]}")
print("-----------------------")

print(f"\nAverage Marks: {average:.2f}")
print(f"Highest Marks: {highest}")
print(f"Lowest Marks: {lowest}")
print(f"Passed Students ({len(passed)}): {', '.join(passed)}")
print(f"Failed Students ({len(failed)}): {', '.join(failed)}")