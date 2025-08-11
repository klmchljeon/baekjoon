t = int(input())
for case in range(t):
    n,k = map(int,input().split())
    lst = list(map(int,input().split()))
    cnt = 0
    for i in lst:
        cnt += i//k
        
    print(cnt)