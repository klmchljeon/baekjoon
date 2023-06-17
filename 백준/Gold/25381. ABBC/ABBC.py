#ABBC
st = input()
n = len(st)

a,b,c = [],[],[]

for i in range(n):
    if st[i] == 'A':
        a.append(i)

    elif st[i] == 'B':
        b.append(i)

    else:
        c.append(i)

cnt = 0
while a and b:
    if a[-1] < b[-1]:
        a.pop()
        b.pop()
        cnt += 1

    else:
        a.pop()

while b and c:
    if b[-1] < c[-1]:
        b.pop()
        c.pop()
        cnt += 1

    else:
        b.pop()

print(cnt)