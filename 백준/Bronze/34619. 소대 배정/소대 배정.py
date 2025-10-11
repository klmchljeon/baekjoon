a,b,n,k = map(int,input().split())
m = (k-1)//n + 1
p,q = divmod(m-1,b)
print(p+1,q+1)