import sys
input = sys.stdin.readline

n = int(input())
lst = []
for _ in range(n):
    tmp = list(map(int,input().split()))
    lst.append(tmp)

m = 5
res = -1
val = [0]*5
for i in range(m-1):
    for j in range(i+1,m):
        cnt = 0
        for idx in range(n):
            cnt += lst[idx][i] and lst[idx][j]

        if res < cnt:
            res = cnt
            val = [0]*5
            val[i] = val[j] = 1

print(res)
print(*val)