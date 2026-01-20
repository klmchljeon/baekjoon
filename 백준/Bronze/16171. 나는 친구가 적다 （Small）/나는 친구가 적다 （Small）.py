s = input()
t = input()
res = ''
for i in s:
    res += '' if '0'<=i<='9' else i

print(int(t in res))