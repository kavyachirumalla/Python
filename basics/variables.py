print(input("enter your name: "))
age = input("enter your age: ")
print("your age is: " + age)
print(int(input("enter a value: ")))
print(int(input("enter b value: ")))
a=int(input("enter a value: "))
b=int(input("enter b value: "))
print("the sum is: " + str(a+b))
print("the difference is: " + str(a-b))
n=int(input("enter n value: "))
for i in range(1,n+1):
    if i%3==0:
        continue
    print(i)

m=int(input("enter m value: "))
for i in range(1,m+1):
    if i%5==0:
        continue
    print(i)
n=int(input("enter n value: "))
for i in range(1,n+1):
    print(i)
k=int(input("enter k value: "))
for i in range(1,k+1):
    if i%2==0:
        print(i)
l=int(input("enter l value: "))
for i in range(1,l+1):
    if i%4==0:
        continue
    print(i)
p=int(input("enter p value: "))
for i in range(1,p+1):
    if i%6==0:
        break
    print(i)
q=int(input("enter q value: "))
while q>=1:
    print(q)
    q=q-1

r=int(input("enter r value: "))
total=0
for i in range(1,r+1):
    if i%2!=0:
        total=total+i

print("sum of odd numbers:",total)

s=int(input("enter s value: "))
limit=s/2

for i in range(1,s+1):
    if i>limit:
        break
    print(i)