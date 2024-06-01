t = int(input())
for i in range(t):
    n,m = map(int,input().split())
    s = 1
    for i in range(1,n+1):
        s*=(i+m-n)/i
    print(round(s))