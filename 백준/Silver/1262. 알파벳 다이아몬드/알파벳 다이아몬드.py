def find(loc):
    x,y = loc
    r,c = map(f,(x,y))
    dist = abs(x-r) + abs(y-c)
    if dist >= n:
        return '.'
    else:
        return alpha[dist%26]
    
f = lambda x:(x//leng)*leng + n-1

alpha = [chr(i + ord('a')) for i in range(26)]

n,r1,c1,r2,c2 = map(int,input().split())
leng = n*2 - 1

res = []
for i in range(r1,r2+1):
    tmp = []
    for j in range(c1,c2+1):
        tmp.append(find((i,j)))
    
    res.append(''.join(tmp))

print('\n'.join(res))