n = int(input())
d = input()

r = d.count('R')
b = d.count('B')

res = min(r,b)
tmp = r if d[0]=='R' else b
cnt = 0
for i in range(n):
    if d[i] != d[0]:
        res = min(res, tmp-cnt)
        break
        
    cnt += 1

tmp = r if d[n-1]=='R' else b
cnt = 0
for i in range(n-1,-1,-1):
    if d[i] != d[n-1]:
        res = min(res, tmp-cnt)
        break
        
    cnt += 1
    
print(res)