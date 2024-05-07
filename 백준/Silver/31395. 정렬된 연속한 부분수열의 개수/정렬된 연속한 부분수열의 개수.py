n = int(input())
d = list(map(int,input().split())) + [0]

cnt = 1
res = 0
for i in range(1,n+1):
    if d[i-1] < d[i]:
        cnt += 1

    else:
        res += cnt*(cnt+1)//2
        cnt = 1

print(res)