import sys
input = sys.stdin.readline

def format_(a,b):
    return f'({a},{b})'

def f1(n,k):
    return (n-1)%(k+1) != 0

def f2(n,k):
    return (n-1)%(2*k+2) > 1

def f3(n,k):
    m = (n-1)%(2*k+2)
    return 0 < m <= k+1

lst = [f1,f2,f3]
p = [((2,4),(1,3)),((3,4),(1,2)),((2,3),(1,4))]

t = int(input())
for case in range(t):
    n,k = map(int,input().split())
    if k == 1:
        m = (n-1)%4 + 1
        res = []
        for i in range(1,4):
            for j in range(i+1,5):
                if i==m or j==m: continue
                res.append(format_(i,j))

    else:
        res = []
        for i in range(3):
            res.append(format_(*p[i][lst[i](n,k)]))

    print(*sorted(res))