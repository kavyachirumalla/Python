class Student:
    def __init__(self,name,roll):
        self.name=name
        self.roll=roll
    def display(self):
        print("name:",self.name)
        print("rollno:",self.roll)
s1=Student("kavya",20)
s2=Student("anu",21)
s1.display()
s2.display()

class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    def annual_salary(self):
        return self.salary*12
    def display(self):
        print("name:",self.name)
        print("annual_salary:",self.annual_salary())
E1=Employee("kavya",20000)
E1.display()

class BankAccount:
    def __init__(self,name,balance):
        self.name=name
        self.balance=balance
    def deposit(self,amount):
        self.balance+=amount
    def withdraw(self,amount):
        if amount>self.balance:
            print("insufficient balance")
        else:
            self.balance-=amount
    def display(self):
        print("name:",self.name)
        print("balance:",self.balance)
b1=BankAccount("kavya",5000)
b1.deposit(1000)
b1.withdraw(2000)
b1.display()

class Person:
        def introduce(self):
            print("iam a person")
class Student(Person):
    def study(self):
        print("iam studying")
s1=Student()
s1.introduce()
s1.study()

class Dog:
    def sound(self):
        print("bark")
class Cat:
    def sound(self):
        print("moow")
d=Dog()
c=Cat()
d.sound()
c.sound()

class Account:
    def __init__(self,balance):
        self.__balance=balance
    def deposit(self,amt):
        self.__balance=+amt
    def withdraw(self,amt):
        self.__balance=-amt
    def get_balance(self):
        return self.__balance
a=Account(5000)

class Vehicle:
    def move(self):
        print("vehicle moving")
class Car(Vehicle):
    def move(self):
        print("car driving")
c=Car()
c.move()

class Vehicle:
    def move(self):
        print("vehicle moving")
class Car(Vehicle):
    def move(self):
        super().move()
        print("car driving")
c=Car()
c.move()

class Person:
    def __init__(self,name):
        self.name=name
class Employee(Person):
    def __init__(self,name,salary):
        super().__init__(name)
        self.salary=salary
E=Employee("kavya",20000)
print(E.name)
print(E.salary)

class Calculator:
    @staticmethod
    def multiply(a,b):
        return a*b
print(Calculator.multiply(3,6))

class Student:
    college="vaagdevi"
    @classmethod
    def change_name(cls,new_name):
        cls.college=new_name
Student.change_name("kits")
print(Student.college)

class Book:
    def __init__(self,title,price):
        self.title=title
        self.price=price
    def __str__(self):
        return f"The title of book is {self.title} and price is {self.price}"
b=Book("The art of being alone",500)
print(b)

class Mobile:
    def __init__(self,battery):
        self.__battery=battery
    def charge(self,amount):
        if amount>0:
            self.__battery+=amount
    def use(self,amount):
        if amount>0:
            self.__battery-=amount
        else:
            print("no charging")
    def get_battery(self):
        return self.__battery
    def __str__(self):
        return f"The battery present is {self.__battery}"
m=Mobile(80)
m.charge(20)
m.use(60)
print(m)