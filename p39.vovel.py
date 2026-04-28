# 17. Write a program to see if the entered letter is a vowel or a consonant.
# Example:
# •	Enter letter => a
# •	Output: a is a vowel;
# •	Enter letter => h
# •	Output: h is a consonant.

ch=input("enter char")

ch=ch.lower()

if(ch=='a'or ch=='e' or ch=='i' or ch=='o' or ch=='u'):
    print("vovel")
else:
    print("consonant")    