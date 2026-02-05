n=int(input("enter n value:"))
list=[]
for i in range(1,n+1):
    list.append(i)
print(list)

m=int(input("enter values:"))
list=[]
for i in range(m):
    value=int(input())
    list.append(value)

even_list=[]
for num in list:
    if num%2==0:
        even_list.append(num)
print(even_list)

lst=[]
p=int(input("enter p value "))
for i in range(p):
    value=int(input())
    lst.append(value)
total=0
for x in lst:
    total=total+x

print(total)

lst=[]
n=int(input("enter n value:"))
for i in range(n):
    value=int(input())
    lst.append(value)
count=0
cou=0
for x in lst:
    if x%2==0:
        count=count+1
print(count)
for x in lst:
    if x%2==1:
        cou=cou+1
print(cou)

lst=[]
n=int(input("enter n value:"))
for i in range(n):
    value=int(input())
    lst.append(value)
max_value=lst[0]
for x in lst:
    if x>max_value:
        max_value=x
print(max_value)

lst=[]
n=int(input("enter n value:"))
for i in range(n):
    value=int(input())
    lst.append(value)
rev=[]
for x in lst:
    rev.insert(0,x)
print(rev)

lst=[]
u=int(input("enter u value:"))
for i in range(u):
    lst.append(int(input()))
unique=[]
for x in lst:
    if x not in unique:
        unique.append(x)
print(unique)

lst=[]
r=int(input("enter r value:"))
for i in range(r):
    lst.append(int(input()))
positive=0
negative=0
zero=0
for x in lst:
    if x>0:
        positive=positive+1
    if x<0:
        negative=negative+1
    if x==0:
        zero=zero+1
print(positive)
print(negative)
print(zero)

lst=[]
d=int(input("enter d value:"))
for i in range(d):
    lst.append(int(input()))
even_list=[]
odd_list=[]
for x in lst:
    if x%2==0:
        even_list.append(x)
    if x%2==1:
        odd_list.append(x)
print(even_list)
print(odd_list)


lst=[]
n=int(input("enter n value:"))
for i in range(1,n+1):
    lst.append(int(input()))
m=int(input("enter m value:"))
result=[]
for x in lst:
    if x!=m:
        result.append(x)
print(result)

lst=[1,2,3,4,5]
max1=lst[0]
max2=-1
for x in lst:
    if x>max1:
        max2=max1
        max1=x
    elif x>max2 and x!=max1:
        max2=x
print(max2)

lst=[1,1,2,2,3,3,4]
freq={}
for x in lst:
    if x in freq:
        freq[x]=freq[x]+1
    else:
        freq[x]=1
print(freq)

lst=[1,3,4,2,5]
is_sorted=True
for i in range(len(lst)-1):
    if lst[i]>lst[i+1]:
        is_sorted=False
        break
if is_sorted:
        print("sorted")
else:
        print("not sorted")

lst=[5,4,3,2,1]
result=[]
for x in lst:
    if x%2==0:
        result.append(x*x)
print(result)