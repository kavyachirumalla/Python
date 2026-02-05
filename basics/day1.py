n=int(input("enter n value: "))
for i in range(1,n+1):
    if i%3==0:
        continue
    if i==11:
       break
    print(i)

m=int(input("enter m value: "))
count=0
for i in range(1,m+1):
    if i%2==0:
        count=count+1
print("count of even numbers:",count)

k=int(input("enter k value: "))
for i in range(1,k+1):
    if i%7==0:
        break
    print(i)

l=int(input("enter l value:"))
while l>=1:
    print(l)
    l=l-2
n=int(input("enter n value:"))
for i in range(1,n+1):
    if i%4==0:
        continue
    if i==15:
        break
    print(i)

n=int(input("enter n value:"))
while n>=1:
    if n%2!=0:
        print(n)
    n=n-1

e=int(input("enter e value:"))
sum=0
for i in range(1,e+1):
    if i%2==0:
     sum=sum+i
     
print(f"the sum is:{sum}")