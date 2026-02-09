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

arr = [2, 1, 5, 1, 3, 2]
k = 3

window_sum = 0
max_sum = 0
for i in range(k):
    window_sum += arr[i]

max_sum = window_sum
for i in range(k, len(arr)):
    window_sum = window_sum - arr[i - k]  
    window_sum = window_sum + arr[i]      

    if window_sum > max_sum:
        max_sum = window_sum

print(max_sum)

arr = [1, 3, 2, 6, -1, 4, 1, 8, 2]
k = 5

window_sum = 0
result = []
for i in range(k):
    window_sum += arr[i]

result.append(window_sum / k)

for i in range(k, len(arr)):
    window_sum = window_sum - arr[i - k]
    window_sum = window_sum + arr[i]
    result.append(window_sum / k)

print(result)

s = "abcabcbb"

char_set = set()
l = 0
max_length = 0

for r in range(len(s)):
    while s[r] in char_set:
        char_set.remove(s[l])
        l += 1

    char_set.add(s[r])
    max_length = max(max_length, r - l + 1)

print(max_length)

s = "araaci"
k = 2

freq = {}
l = 0
max_len = 0

for r in range(len(s)):
    freq[s[r]] = freq.get(s[r], 0) + 1

    while len(freq) > k:
        freq[s[l]] -= 1
        if freq[s[l]] == 0:
            del freq[s[l]]
        l += 1

    max_len = max(max_len, r - l + 1)

print(max_len)

arr = [2, 1, 5, 2, 3, 2]
S = 7

l = 0
window_sum = 0
min_length = float('inf')

for r in range(len(arr)):
    window_sum += arr[r]

    while window_sum >= S:
        min_length = min(min_length, r - l + 1)
        window_sum -= arr[l]
        l += 1

print(min_length)

arr = [2, 4, 1, 3]

prefix = [0] * len(arr)
prefix[0] = arr[0]

for i in range(1, len(arr)):
    prefix[i] = prefix[i-1] + arr[i]

l = 1
r = 3

if l == 0:
    result = prefix[r]
else:
    result = prefix[r] - prefix[l-1]

print(result)

def print_desc(n):
    if n == 0:
        return
    print(n)
    print_desc(n - 1)

print_desc(5)

def sum_n(n):
    if n == 0:
        return 0
    return n + sum_n(n - 1)

print(sum_n(5))

def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)

print(factorial(4))

def reverse_str(s):
    if s == "":
        return ""
    return reverse_str(s[1:]) + s[0]

print(reverse_str("abc"))

def is_palindrome(s):
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return False
    return is_palindrome(s[1:-1])

print(is_palindrome("madam"))

def power(base, exp):
    if exp == 0:
        return 1
    return base * power(base, exp - 1)

print(power(2, 4))

def count_digits(n):
    if n == 0:
        return 0
    return 1 + count_digits(n // 10)

print(count_digits(12345))

def sum_digits(n):
    if n == 0:
        return 0
    return (n % 10) + sum_digits(n // 10)

print(sum_digits(1234))