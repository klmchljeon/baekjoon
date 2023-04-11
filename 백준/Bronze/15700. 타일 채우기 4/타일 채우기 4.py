n,m = map(int,input().split())
res = (n*m - (n*m)%2)//2
print(res)