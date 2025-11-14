# basic example of for loop
marks=[1,2,3,4,5,6,7,8]
for m in marks:
    print(m)
    
# basic example of if else
marks=[30,40,50,60,80]
for m in marks:
    if m>=40:
        print("pass")
    else:
        print("fail")


#basic method to find average 
numbers = [10, 20, 30, 40, 50]
total=0
count=0
for n in numbers:
    total+=n
    count+=1
average=total/count
print(count)
print(total)
print(f"The average of list is:{average}")