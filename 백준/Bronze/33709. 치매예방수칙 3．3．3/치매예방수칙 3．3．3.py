n = int(input())
st = input()
lst = []
tmp = ''
for i in st:
    if '0'<=i<='9':
        tmp += i
    else:
        lst.append(int(tmp))
        tmp = ''

if tmp:
    lst.append(int(tmp))

print(sum(lst))