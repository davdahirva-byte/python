# 8. Enter marks for 3 subjects, print total, and if total > 50, then display "Pass", else display "Fail".
# Example:
# •	Enter marks of Hindi => 22
# •	Enter marks of English => 30
# •	Enter marks of SS => 35
# •	Output: Your total is 87. You are Pass.


hindi_marks=int(input("enter hindi marks"))
english_marks=int(input("enter english marks"))
ss_marks=int(input("ss marks"))

total=hindi_marks+english_marks+ss_marks

print(total,"total")
