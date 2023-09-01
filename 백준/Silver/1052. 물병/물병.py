#물병
n,k = map(int,input().split())

t = n
while True:
    cnt = 0
    for i in range(24):
        if t&(1<<i):
            cnt += 1

    if k >= cnt: 
        print(t-n)
        break

    for i in range(24):
        if t&(1<<i):
            fir = i
            break

    for i in range(fir+1,24):
        if t&(1<<i):
            t += (1<<i) - (1<<fir)
            break