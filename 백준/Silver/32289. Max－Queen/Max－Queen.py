n,m = map(int,input().split())
res = (n-2)*(m-2)*4
res += (n-1)*3
res += (m-2)*4
res += (n-1)*2
res += (m-1)

print(res)