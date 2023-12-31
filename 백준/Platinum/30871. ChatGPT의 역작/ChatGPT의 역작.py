v = 81985529216486895

def f(x):
    value = x
    for i in range(n):
        le = l[i]
        ri = r[i]
        if le <= x <= ri:
            value = value^(((x|le)+(x&ri)*(le^ri))%(2**64))

    return value >= v

n = int(input())
l = list(map(int,input().split()))
r = list(map(int,input().split()))

s,e = 0,10**18+1
while s+1<e:
    mid = (s+e)//2

    if not f(mid):
        s = mid
    
    else:
        e = mid

print(s)