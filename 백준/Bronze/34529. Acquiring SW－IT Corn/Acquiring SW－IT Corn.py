f = lambda a,b,c:(b//c + bool(b%c))*a

x,y,z = map(int,input().split())
u,v,w = map(int,input().split())

res = 0
res += f(x,u,100)
res += f(y,v,50)
res += f(z,w,20)
print(res)