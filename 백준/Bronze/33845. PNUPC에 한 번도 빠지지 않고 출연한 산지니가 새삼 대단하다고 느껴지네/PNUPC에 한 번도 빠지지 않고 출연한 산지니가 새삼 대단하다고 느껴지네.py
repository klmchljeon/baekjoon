s = input()
t = input()
res = ''
for i in t:
    if not i in s:
        res += i

print(res)