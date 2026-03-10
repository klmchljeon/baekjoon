p = int(input())
for case in range(p):
    n,d,a,b,f = map(float,input().split())
    s = d/(a+b)
    print(int(n),s*f)