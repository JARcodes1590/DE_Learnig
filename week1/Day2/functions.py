def add(a,b):
    return a+b
# print(add(19,22))

def square(n):
    return n*n
result=square(4)
# print(result)

def average(numbers):
    count=0
    total=0
    for n in numbers:
        total+=n
        count+=1
    return total/count
        

# print(average([10, 20, 30]))   # 20.0
# print(average([5, 5, 5, 5]))   # 5.0


def get_stats(numbers):
    min_num=numbers[0]
    max_num=numbers[0]
    total=0
    count=0
    for s in numbers:
        total+=s
        count+=1
        if s<min_num:
            min_num=s
        if s>max_num:
            max_num=s
    ave=total/count
    return min_num,max_num,ave
mn, mx, avg = get_stats([14, 3, 9, 27, 18, 5])
# print(mn, mx, avg)



def get_top_student(students):
    top_student=students[0]
    for s in students[1:]:
        if s["marks"]> top_student["marks"]:
            top_student=s
            
    return top_student["name"],top_student["marks"]
def count_pass_fail_students(students,pass_mark):
    passed=0
    failed=0
    
    for n in students:
        if n["marks"]>=pass_mark:
            passed+=1
        else:
            failed+=1
    return passed,failed
students = [
    {"name": "Asha", "age": 20, "marks": 85},
    {"name": "Bikash", "age": 22, "marks": 75},
    {"name": "Chandra", "age": 21, "marks": 90},
    {"name": "Deepa", "age": 23, "marks": 60},
]
# name, marks = get_top_student(students)
# print("Top student:", name, marks)

# passed, failed = count_pass_fail_students(students, 70)
# print("Passed:", passed, "Failed:", failed)

