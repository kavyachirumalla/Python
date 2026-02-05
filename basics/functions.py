def add(a,b):
    return a+b

print(add(2,3))

def square(a):
    return a*a
print(square(6))

def even_or_odd(a):
    if a%2==0:
        return "even"
    else:
        return "odd"
print(even_or_odd(7))

def large(a,b):
    if a>b:
        return a
    else:
        return b
print(large(5,6))

def add(n):
    sum=0
    for i in range(1,n+1):
        sum=sum+i
    return sum
print(add(5))

def add(lst):
    sum=0
    for x in lst:
        sum=sum+x
    return sum
print(add([1,2,3,4,5]))

def even(lst):
    result=[]
    for x in lst:
        if x%2==0:
            result.append(x)
    return result
print(even([1,2,3,4,5,6]))

def positive(a):
    if a>0:
        return True
    else:
        return False
    
print(positive(-1))

def vowels(string):
    count=0
    for char in string:
        if (char=="a" or char=="e" or char=="i" or char=="o" or char=="u"):
         count=count+1
    return count
print(vowels("kavya"))

def maxm(lst):
    max=lst[0]
    for x in lst:
        if x>max:
            max=x
    return max
print(maxm([1,3,6,9]))


def maxm(lst):
    if not lst:
        return None
    max=lst[0]
    for x in lst:
        if x>max:
            max=x
    return max
print(maxm([1,4,5,6,7]))

def greater(lst):
    result=[]
    for x in lst:
        if x>10:
            result.append(x)
    return result
print(greater([1,2,30,40,60,90,7]))

def prime(a):
    if a<=1:
        return False
    for i in range(2,a):
     if a%i==0:
        return False
    return True
print(prime(7))

def is_even(n):
        return n%2==0
def get_even(lst):
    result=[]
    for x in lst:
        if is_even(x):
            result.append(x)
    return result
print(get_even([1,3,5,6,7,8,9]))