n,m = map(int,input().split())
d = []
for i in range(1,m+1):
    a,b = map(int,input().split())
    d.append((a,i))
    d.append((b,i))

d.sort()

print((d*n)[n-1][1])