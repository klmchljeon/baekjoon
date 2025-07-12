t = int(input())
for case in range(t):
    l,r,s = map(int,input().split())

    a = (s-l)*2
    b = (r-s)*2 - 1
    print(min(a,b)+1)