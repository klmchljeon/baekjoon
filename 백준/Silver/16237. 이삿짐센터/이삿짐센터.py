a,b,c,d,e = map(int,input().split())
res = c + d + e
a -= min(a,d)

tmp = min(b,c)
b -= tmp
c -= tmp

a -= min(a,c*2)

tmp = b//2
res += tmp
b -= tmp*2
a -= min(a,tmp)

p = b*2 + a
res += p//5 + bool(p%5)
print(res)