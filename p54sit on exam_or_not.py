# 30. A student will not be allowed to sit in the exam if his/her attendance is less than 75%.
# Take the following input from the user:
# •	Number of classes held
# •	Number of classes attended Print the percentage of classes attended:
# •	Formula: (Number of classes attended / float(Number of classes held)) * 100 Output: Is the student allowed to sit in the exam or not
# 
# .

held=int(input("enter number of classes held"))
attendance=int(input("enter attendance"))

percentage=attendance/held*100

print(percentage)

if percentage<75:
    print("not allowed")
else:
    print("allowed")    
