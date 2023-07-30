#문자열 폭발
s = input()
b = input(); lenb = len(b)

d = []
cs = 0
pre = []

result = []

for i in s:
    result.append(i)
    if i == b[cs]:
        d.append(i)
        cs += 1

    elif i == b[0]:
        d.append(i)
        pre.append(cs)
        cs = 1

    else:
        d = []
        cs = 0
        pre = []

    if cs == lenb:
        for _ in range(lenb):
            result.pop()
            d.pop()

        cs = 0 if not pre else pre.pop()

if result:
    print(*result,sep='')
else:
    print('FRULA')