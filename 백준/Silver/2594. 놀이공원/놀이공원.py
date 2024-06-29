def conv(time):
    a,b = divmod(time,100)
    return a*60 + b

n = int(input())
lst = [1]*(24*60 + 1)
for _ in range(n):
    p = map(int,input().split())
    
    d = []
    for i in p:
        d.append(conv(i))
    
    for i in range(d[0]-10,d[1]+10):
        lst[i] = 0

res = 0
tmp = 0
for i in range(conv(1000),conv(2200)):
    tmp += lst[i]
    if lst[i] == 0 and lst[i-1] == 1:
        res = max(res,tmp)
        tmp = 0

res = max(res,tmp)

print(res)