import sys
input = sys.stdin.readline

n = int(input())
lst = []
for _ in range(n):
    a,b = map(int,input().split())
    lst.append((a,b))

lst.sort(key = lambda x:(x[1],x[0]))
res = 0
for i in range(1,n):
    cnt = 0
    for j in range(i):
        cnt += lst[i][0] <= lst[j][0]

    res = max(res,cnt)

print(res)