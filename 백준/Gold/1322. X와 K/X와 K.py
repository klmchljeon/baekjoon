x,k = map(int,input().split())
tmp = x
i = 0
idx = 0
while 1<<i <= k:
    while x&(1<<idx):
        idx += 1

    x |= (1<<idx) * bool(k&(1<<i))
    i += 1
    idx += 1

print(x&(~tmp))