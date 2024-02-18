n = int(input())
d = []
for _ in range(n):
    d.append([input() for _ in range(5)])

res = [-1,-1,-1]
for i in range(n-1):
    for j in range(i+1,n):
        cnt = 0
        for x in range(5):
            for y in range(7):
                cnt += d[i][x][y]==d[j][x][y]

        if res[0] < cnt:
            res = [cnt,i,j]

print(res[1]+1,res[2]+1)