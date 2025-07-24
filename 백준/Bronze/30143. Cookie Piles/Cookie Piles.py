t = int(input())
for case in range(t):
    n,a,d = map(int,input().split())
    print(n*a + d*n*(n-1)//2)