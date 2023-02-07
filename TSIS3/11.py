def palindrome(s):
    r = s[::-1]
    if s == r:
        return "YES"
    else:
        return "NO"
s = input()
print(palindrome(s))

'''
s = input()
i = 0
j = len(s) - 1
palindrom = True
while i < j:
    if s[i] != s[j]:
        palindrom = False
    i += 1
    j -= 1
if palindrom == True:
    print('YES')
else:
    print("NO")
'''
