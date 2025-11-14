students = [
    {"name": "Asha", "age": 20, "marks": 85},
    {"name": "Bikash", "age": 22, "marks": 75},
    {"name": "Chandra", "age": 21, "marks": 90},
    {"name": "Deepa", "age": 23, "marks": 60},
]

total=0
count=0
min_value=students[0]["marks"]
max_value=students[0]["marks"]
for s in students:
    total+=s["marks"]
    count+=1
    if s["marks"]>max_value:
        max_value=s["marks"]
    if s["marks"]<min_value:
        min_value=s["marks"]
average=total/count

print(f"maximum={max_value},minimum={min_value},average={average}")


passed=0
failed=0
pass_mark=70
for n in students:
    if n["marks"]>=pass_mark:
        passed+=1
        print(f'{n["name"]} {n["marks"]} pass')
    else:
        failed+=1
        
print(f"Hence {passed} number of student is passed and {failed} no of student is failed")
    