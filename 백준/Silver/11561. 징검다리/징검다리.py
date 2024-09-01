def check(num):
    tmp = num*(num+1)//2
    return tmp <= n

t = int(input())
for case in range(t):
    n = int(input())
    
    s,e = 1,n+1
    while s+1<e:
        mid = (s+e)//2

        if check(mid):
            s = mid

        else:
            e = mid

    print(s)