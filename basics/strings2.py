s="success"
freq={}
for ch in s:
    freq[ch]=freq.get(ch,0)+1
print(freq)

s="swiss"
freq={}
for ch in s:
    freq[ch]=freq.get(ch,0)+1
for ch in s:
    if freq[ch]==1:
     print(ch)
     break

s="programming"
result=""
for ch in s:
   if ch not in result:
      result+=ch
print(result)

s="i love python"
words=s.split()
words=words[::-1]
result="".join(words)
print(result)

s1="listen"
s2="silent"

if len(s1)!=len(s2):
   print("not anagram")
else:
   freq={}
   for ch in s1:
      freq[ch]=freq.get(ch,0)+1
for ch in s2:
   if ch not in freq:
      print("not anagram")
      break
   freq[ch]-=1
else:
    if all (v==0 for v in freq.values()):
      print("anagram")
    else:
      print("not anagram")

s="i love python"
words=s.split()
count=0
for w in words:
   count+=1
print(count)

s="programming"
freq={}
for ch in s:
   freq[ch]=freq.get(ch,0)+1

max_char=""
max_count=0
for ch in s:
   if freq[ch]>max_count:
      max_count=freq[ch]
      max_char=ch
print(max_char)

s="hello"
freq={}
for ch in s:
   freq[ch]=freq.get(ch,0)+1

unique=True
for ch in freq:
 if freq[ch]>1:
    unique=False

if unique:
    print(" unique")
else:
    print("not unique")
      