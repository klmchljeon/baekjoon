n = int(input())
lst = list(map(int,input().split()))
res = 0
for i in range(1,n+1):
    flag = False
    cnt = 0
    for j in range(2*n):
        if lst[j] == i:
            flag ^= True
            continue

        cnt += flag

    res = max(res,cnt)

print(res)