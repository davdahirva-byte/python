# 29. Using the following list of programming languages per paradigm:

# procedural = ["c", "fortran", "pascal"]
# object_oriented = ["java", "c++", "python"]
# functional = ["haskell", "scala", "lisp"]

# Write a program that asks the user to enter a programming language and tells them which paradigm it belongs to.

procedural = ["c", "fortran", "pascal"]
object_oriented = ["java", "c++", "python"]
functional = ["haskell", "scala", "lisp"]

language=input("enter the language => ")

if language in procedural:
    print("procedural")
elif language in object_oriented:
    print("object_oriented")
elif language in functional:
    print("functional")
else:
    print("language not found")    

