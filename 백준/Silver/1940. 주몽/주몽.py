#주몽
n = int(input())
m = int(input())
d = list(map(int,input().split()))
d.sort()

cnt = 0

s,e = 0,n-1
while s<e:
    if d[s]+d[e] >= m:
        cnt += d[s]+d[e]==m
        e -= 1
    
    else:
        s += 1

print(cnt)