t = int(input())
for case in range(t):
    n,*lst = map(int,input().split())
    
    m = None
    cnt = 0
    for i in lst:
        if cnt == 0:
            m = i
            cnt += 1

        elif i == m:
            cnt += 1
        else:
            cnt -= 1

    tmp = 0
    for i in lst:
        tmp += i==m

    if tmp > n//2:
        print(m)
    else:
        print('SYJKGW')