s=list("kavya")
l=0
r=4
while l<r:
    s[l],s[r]=s[r],s[l]
    l+=1
    r-=1
print("".join(s))

s="12121"
l=0
r=len(s)-1
is_palindrome=True

while l<r:
    if s[l]!=s[r]:
     is_palindrome=False
     break
    l+=1
    r-=1
if is_palindrome:
    print("palindrome")
else:
    print("not a palindrome")

s="n u r s e s r u n"
l=0
r=len(s)-1
is_palindrome=True
while l<r:
   if s[l]==" ":
      l+=1
      r-=1
      continue
   if s[r]==" ":
      l+=1
      r-=1
      continue
   if s[l]!=s[r]:
      is_palindrome=False
      break
   l+=1
   r-=1
if is_palindrome:
   print("palindrome")
else:
   print("not a palindrome")


arr=[1,2,3,4,6]
k=6
l=0
r=len(arr)-1
found=False
while l<r:
   s=arr[l]+arr[r]
   if s==k:
      found=True
      break
   elif s<k:
      l+=1
   else:
      r-=1
if found:
   print("pair exists")
else:
   print("no pair")

s=list("123456")
l=0
r=(len(s)//2)-1
while l<r:
    s[l],s[r]=s[r],s[l]
    l+=1
    r-=1
print("".join(s))

s="i love python"
words=s.split()
l=0
r=len(words)-1
while l<r:
   words[l],words[r]=words[r],words[l]
   l+=1
   r-=1
print("".join(words))
      