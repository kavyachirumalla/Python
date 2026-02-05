student={
    "name":"kavya",
    "age":20,
    "branch":"csm",
}
print(student["name"])
print(student["age"])

student["college"]="vec"
student["age"]=21
print(student)

if "branch" in student:
    print("exists")
else:
    print("doesnt exist")

if "marks" in student:
    print("exists")
else:
    print("doesnt exist")

marks={
    "maths":80,
    "phy":70,
    "chem":50,
}
print(marks["maths"])

for key in student:
    print(key)

for value in student.values():
    print(value)
for key,value in student.items():
    print(key,value)

lst=[1,3,3,4,5,6,7,8,7]
freq={}
for x in lst:
    if x in freq:
        freq[x]=freq[x]+1
    else:
        freq[x]=1
print(freq)

marks={
    "math":90,
    "phy":70,
    "chem":50,
}
max_marks=-1
top_subject=""
for key,value in marks.items():
    if value>max_marks:
        max_marks=value
        top_subject=key

print(top_subject,max_marks)

student={
    "name":"kavya",
    "marks":{
        "maths":90,
        "phy":80,
    }
}
print(student["marks"]["phy"])