#주사위

n = int(input())
d = list(map(int,input().split()))
mind = [min(d[0],d[5]),min(d[1],d[4]),min(d[2],d[3])]
mind.sort()

if n == 1:
    print(sum(d) - max(d))
    exit(0)

v = 4 * sum(mind)
e = (8*(n-2)+4) * sum(mind[:-1])
f = (5*(n-2)+4)*(n-2) * mind[0]
print(v+e+f)