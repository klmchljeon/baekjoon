#
n = int(input())
d = []
for _ in range(n):
    a,b = map(int,input().split())
    d.append((a,b))

f = lambda x:(-x[0],x[1])
d.sort(key=f)

tmp = d[4][0]
cnt = 0
for i in range(5,n):
    if d[i][0] != tmp: 
        break

    cnt += 1

print(cnt)