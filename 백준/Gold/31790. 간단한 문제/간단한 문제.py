n,p = map(int,input().split())
lst = list(map(int,input().split()))
if lst[0] != 1:
    print('NO')
    exit()

k = n//p + bool(n%p)
m = 1
cnt = 0
for i in range(1,n):
    if lst[i] - lst[i-1] == 1:
        if m == k:
            print('NO')
            break

        m += 1

    elif lst[i] - lst[i-1] == 0:
        cnt += 1
        cur = (i+1)//p + bool((i+1)%p)
        if cur > m:
            print('NO')
            break

    else:
        print('NO')
        break

else:
    if cnt == n-k:
        print('YES')
    else:
        print('NO')