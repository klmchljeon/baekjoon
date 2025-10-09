n,t = map(int,input().split())
st = input()

l = 2**(n-t)
res = 0
for i in range(0,len(st),l):
    res = max(res,int(st[i:i+l]))

print(res)