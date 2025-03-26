n,m = map(int,input().split())
lst = []
for _ in range(n):
    lst.append(int(input()))

p = []
for _ in range(m):
    p.append(int(input()))

cur = 0
for i in range(m):
    val = p[i]
    cur += val
    if cur >= n-1: 
        print(i+1)
        break

    cur = cur + lst[cur]
    if cur >= n-1:
        print(i+1)
        break