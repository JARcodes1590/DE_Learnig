from functions import get_top_student,count_pass_fail_students
students = []
with open("/home/raj/Desktop/DE_base/week1/Day2/students.csv", "r", encoding="utf-8") as f:
    header = f.readline()  # read the first line (column names)
    for line in f:
        line = line.strip()          # remove \n
        if not line:                 # skip empty lines
            continue
        name, age_str, marks_str = line.split(",")
        student = {
            "name": name,
            "age": int(age_str),
            "marks": int(marks_str),
        }
        students.append(student)

name, marks = get_top_student(students)
print("Top student:", name, marks)

passed, failed = count_pass_fail_students(students, 70)
print("Passed:", passed, "Failed:", failed)
