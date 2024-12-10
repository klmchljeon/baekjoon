import sys
input = sys.stdin.readline

def check(num):
    return cal(num) >= t

def cal(num):
    cur = num
    for i in range(n):
        cur += p[i]
        a,b,c,d = lst[i]

        cur = max(cur,c)
        x = (cur-c)//a

        if not (cur+d <= c+a*x+b):
            x += 1
            cur = c + a*x

        cur += d

    cur += p[n]
    return cur

tc = int(input())
for case in range(tc):
    n,t = map(int,input().split())
    lst = []
    for _ in range(n):
        a,b,c,d = map(int,input().split())
        lst.append((a,b,c,d))

    p = list(map(int,input().split()))
    
    s,e = -1,t
    while s+1<e:
        mid = (s+e)//2

        if check(mid):
            e = mid
        
        else:
            s = mid

    print('YES' if cal(e) == t else 'NO')