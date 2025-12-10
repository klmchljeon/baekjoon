u,o,s = map(int,input().split())
tmp = max(0,u-s)
print(min(o,min(u,s) + tmp//3))