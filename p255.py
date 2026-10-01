try:
    a=int(input("enter the num"))
    b=int(input("enter the num"))
    c=a/b
    print(c)
except ValueError:
    print("Why u enter string")
except ZeroDivisionError:
    print("Why u enter 0")
except:
    print("Error")