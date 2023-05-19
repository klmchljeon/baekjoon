code = ord('A')-ord('a')

st = input()
lst = input().split()

res = ''
for i in st:
    if i in lst:
        res += chr(ord(i)-code)
    else:
        res += i

print(res)