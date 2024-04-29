n = int(input())
d = list(map(int,input().split()))
tmp = sorted(d)

if d == tmp:
    print(1)
    exit()

cnt = 0
for i in range(1,n):
    cnt += d[i-1]>d[i]

if cnt==1 and d[0]>d[-1]:
    print(2)
else:
    print(3)