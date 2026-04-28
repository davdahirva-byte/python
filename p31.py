# 9. Enter marks for 3 subjects, print total, and display grades based on total:
# •	0-50: C grade
# •	50-100: B grade
# •	100: A grade Example:
# •	Enter marks of Hindi => 22
# •	Enter marks of English => 30
# •	Enter marks of SS => 35
# •	Output: Your total is 87. You got B grade.



hindi_marks=int(input("enter hindi marks"))
english_marks=int(input("enter english marks"))
ss_marks=int(input("ss marks"))

total=hindi_marks+english_marks+ss_marks

if(total<50):
    print("C grade")
elif(total>=50):
    print("B grade")    
elif(total==100):
    print("A grade") 
else:
    print("enter valid") 