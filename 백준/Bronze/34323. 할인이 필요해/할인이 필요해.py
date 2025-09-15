n,m,s = map(int,input().split())
p1 = s*(m+1)*(100-n)//100
p2 = s*m

print(min(p1,p2))