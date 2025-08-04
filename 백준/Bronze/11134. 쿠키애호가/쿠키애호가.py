t = int(input())
for case in range(t):
    n,c = map(int,input().split())
    print(n//c + bool(n%c))