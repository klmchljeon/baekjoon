a = input().split('/')
b = input().split('/')

idx = 0
while idx<len(a) and idx<len(b):
    if a[idx]!=b[idx]: break
    idx += 1

ja = len(a)-1
jb = len(b)-1
while 0<=ja and 0<=jb:
    if a[ja]!=b[jb]: break
    ja -= 1
    jb -= 1

tmpa = []
for i in range(idx,ja+1):
    tmpa.append(a[i])

tmpb = []
for i in range(idx,jb+1):
    tmpb.append(b[i])

res = a[:idx]
res.append('{' + f"{'/'.join(tmpa)} => {'/'.join(tmpb)}" + '}')
res += a[ja+1:]

print('/'.join(res))