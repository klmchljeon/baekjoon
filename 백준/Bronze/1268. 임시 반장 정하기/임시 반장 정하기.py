n = int(input())
d = [list(map(int,input().split())) for _ in range(n)]

res = [[0]*n for _ in range(n)]
for j in range(5):
    lst = [[] for _ in range(10)]
    for i in range(n):
        lst[d[i][j]].append(i)

    for k in range(10):
        for x in lst[k]:
            for y in lst[k]:
                res[x][y] = 1

tmp = [sum(res[i])-1 for i in range(n)]
ans = [-1,0]
for i in range(n):
    if ans[0] < tmp[i]:
        ans = [tmp[i],i+1]

print(ans[1])