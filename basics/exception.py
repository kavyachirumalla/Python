try:
    x=int(input("enter a number"))
    print(100/x)
except ZeroDivisionError:
    print("can't divide by zero")
except ValueError:
    print("invalid input")

age=int(input("enter age"))
if age<18:
    raise ValueError("age must be 18+")

try:
    a=int(input("enter a value"))
    b=int(input("enter b value"))
    sum=a+b
    print(sum)
except ValueError:
    print("enter correct values")

try:
    lst=[10,20,30]
    index=int(input("enter index value"))
    element=lst[index]
    print(element)
except IndexError:
    print("index out of range")
except ValueError:
    print("enter only numbers")

while True:
    try:
        x=int(input("enter a number"))
        print("you entered:",x)
        break
    except ValueError:
        print("invalid,enter again")