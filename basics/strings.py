name=input("enter your name: ")
for char in name:
    print(char)

word=input("enter a word: ")
count=0
for char in word:
    count=count+1
print(f"The length of string is {count}")

string=input("enter a string")
count=0
for char in string:
    if char=='a' or char=='e' or char=='i' or char=='o' or char=='u' or char=='A' or char=='E' or char=='I' or char=='O' or char=='U':
     count=count+1
print(f"The number of vowels are:{count}")

text=input("enter a text: ")
rev=""
for char in text:
   rev=char+rev

print(rev)

text=input("enter text:")
rev=""
for char in text:
   rev=char+rev

if text==rev:
      print("it is a palindrome")
else:
      print("it is not a palindrome")

text=input("enter a text:")
found=False
for char in text:
    count=0
    for c in text:
        if char==c:
            count=count+1

    if count==1:
      print("first non repeatign:",char)
      found=True
      break
if not found:
    print("no non repeating")

a=input("enter a word:")
count=0
con=0
for char in a:
    char=char.lower()
    if char=='':
       continue
    if char=='a' or char=='e' or char=='i' or char=='o' or char=='u':
     count=count+1
    else:
     con=con+1

print(f"The number of vowels are:{count}")
print(f"the number of consonants are:{con}")

string=input("enter a string:")
str=""
for char in string:
   char=char.lower()
   if char=='a' or char=='e' or char=='i' or char=='o' or char=='u':
     continue
   str=str+char
print(f"the string without vowels is:{str}")

word=input("enter a word:")
rev=""
for char in word:
   rev=rev+char
if word==rev:
      print("it is a palindrome")
else:
      print("not a palindrome")