f=open("basics/names.txt","r")
content=f.read()
print(content)

f=open("basics/names.txt","a")
f.write("\nanu\n")
f.write("jaanu\n")
f=open("basics/names.txt","r")
print(f.read())

f=open("basics/numbers.txt","r")
total=0
for line in f:
    total+=int(line.strip())
f.close()
print("sum=",total)

try:
    with open("marks.txt") as f:
        for line in f:
            print(int(line))
except FileNotFoundError:
    print("file not found")
