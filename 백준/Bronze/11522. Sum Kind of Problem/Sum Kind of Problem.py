p = int(input())
for case in range(p):
    k,n = map(int,input().split())
    num = n*(n+1)//2
    res = [k,num,num*2-n,num*2]
    print(*res)