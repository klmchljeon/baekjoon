n = int(input())
x,s = map(int,input().split())
d = []
for _ in range(n):
    c,p = map(int,input().split())
    d.append((c,p))

for c,p in d:
    if c <= x and p > s:
        print('YES')
        break

else:
    print('NO')