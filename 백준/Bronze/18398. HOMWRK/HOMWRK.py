t = int(input())
for case in range(t):
    n = int(input())
    for i in range(n):
        a,b = map(int,input().split())
        print(a+b,a*b)