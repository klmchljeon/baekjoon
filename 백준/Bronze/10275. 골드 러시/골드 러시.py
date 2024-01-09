t = int(input())
for case in range(t):
    n,a,b = map(int,input().split())
    while a%2 == 0:
        a//=2
        n -= 1
        
    print(n)