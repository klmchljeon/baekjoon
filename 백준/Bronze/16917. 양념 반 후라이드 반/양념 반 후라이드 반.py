a,b,c,x,y = map(int,input().split())
p = a*x + b*y
t = min(x,y)
q = c*t*2 + a*(x-t) + b*(y-t)
t = max(x,y)
r = c*t*2
print(min(p,q,r))