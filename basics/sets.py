lst=[1,2,3,4,4,5]
s=set(lst)
print(s)
s.add(10)
s.remove(2)
print(s)
if 8 in s:
    print("exists")
else:
    print("not exists")

a={1,2,3,4}
b={3,4,5,6}
print(a|b)
print(a&b)
print(a-b)