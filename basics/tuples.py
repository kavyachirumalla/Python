from difflib import ndiff


t=(1,2,3,4,5)
print(t[0])
print(t[-1])
print(len(t))

lst=[1,2,3,4,5]
t=(1,2,3,4,5)
lst[0]=2
print(lst)

t=(2,4,6,8,10)
for x in t:
    if x>5:
        print(x)

t=(1,2,3,2,4,2,5)
print(t.count(2))

t=(10,20,30,40,50)
print(t.index(10))

student=("kavya",20,"csm")
name,age,branch=student
print(name)
print(age)
print(branch)

a=10
b=20
t=(20,10)
a,b=t
print("a=",a)
print("b=",b)

def tup():
    a=int(input("enter a "))
    b=int(input("enter b"))
    sum=a+b
    diff=a-b
    return sum,diff
t=tup()
sum,diff=t
print(sum)
print(diff)

points={}
p=(3,4)
distance=(p[0]**2+p[1]**2)**0.5
points[p]=distance
print(points)

t=(95,10,15,20,25)
even_t=()
for x in t:
    if x%2==0:
        even_t=even_t+(x,)
print(even_t)
