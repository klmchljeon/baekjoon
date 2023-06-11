#두 수의 합 04:28
n = int(input())
d = list(map(int,input().split()))
x = int(input())

d.sort()

cnt = 0
s,e = 0,n-1
while s!=e:
    m = d[s]+d[e]
    cnt += m==x

    if m > x:
        e -= 1
    
    else:
        s += 1

print(cnt)