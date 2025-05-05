t = int(input())
for case in range(t):
    a,b = map(int,input().split())
    print(a,b)
    print(a*b - (a-1)*2)