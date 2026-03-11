n = int(input())
lst = []
for _ in range(n):
    tmp = list(map(int,input().split()))
    lst.append(tmp)

res = 0
for i in range(n):
    for j in range(n):
        res += lst[i][j]

print(res)