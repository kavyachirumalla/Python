s="i love python and i love coding"
freq={}
words=s.split()
for w in words:
    freq[w]=freq.get(w,0)+1
print(freq)

lst=[10,5,20,8,15]
max1=0
max2=-1
for x in lst:
    if x>max1:
        max2=max1
        max1=x
    elif x>max2 and x!=max1:
        max2=x
print(max2)

s="engineering"
if len(s)==len(set(s)):
    print("all unique")
else:
    print("not unique")

def remove_vowels(s):
    vowels="aeiouAEIOU"
    result=""
    for ch in s:
        if ch not in vowels:
            result+=ch
    print(result)
remove_vowels("education")

nums=[1,2,3,2,4,1,5,3,2]
freq={}
for x in nums:
    freq[x]=freq.get(x,0)+1
max_count=0
max_num=None
for x in nums:
    if freq[x]>max_count:
        max_count=freq[x]
        max_num=x
print(max_num)


s="placements make placements easy"
freq={}
words=s.split()
for w in words:
    freq[w]=freq.get(w,0)+1
max_count=0
max_word=""
for w in words:
    if freq[w]>max_count:
        max_count=freq[w]
        max_word=w
print(max_word)

lst=[3,7,2,9,5]
min1=lst[0]
min2=0
for x in lst:
    if x<min1:
        min2=min1
        min1=x
    elif x<min2 and x!=min1:
        min2=x
print(min2)

s="career"
unique=""
for ch in s:
    if ch not in unique:
        unique=unique+ch
if len(s)==len(unique):
    print("True")
else:
    print("False")

s1="abcd"
s2="bcda"
if len(s1)==len(s2) and s2 in (s1+s1):
    print("True")
else:
    print("False")

def count_vowels(s):

 vowel="aeiouAEIOU"
 count=0
 for ch in s:
    if ch in vowel:
        count+=1
 print(count)
count_vowels("education")