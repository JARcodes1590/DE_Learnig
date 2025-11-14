numbers = [14, 3, 9, 27, 18, 5]
max_num=numbers[0]
min_num=numbers[0]
total=0
count=0
for n in numbers:
    total+=n
    count+=1
    if n>max_num:
        max_num=n
    if n<min_num:
        min_num=n
average=total/count
print(f"the maximum number in list is {max_num} and the minimum number is {min_num} and average of list is {average}")



marks = [30, 40, 50, 60, 80, 35, 90]
pass_marks=40
passes=0
fails=0
for m in marks:
    if m >= pass_marks:
        passes+=1
    else:
        fails+=1
print(f"The number of passed students is {passes} and number of failed students is {fails}")