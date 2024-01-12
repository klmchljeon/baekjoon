e,f,c = map(int,input().split())

cnt = e + f
res = 0

while cnt >= c:
    res += cnt//c
    cnt = cnt//c + cnt%c

print(res)