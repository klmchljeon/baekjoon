n = int(input())
d = [int(input()) for _ in range(n)]
d.sort()

res = 0
for i in range(n):
    check = [0]*n
    check[i] = 1

    for j in range(i+1,n):
        for k in range(i,j):
            if d[k] + check[k] >= d[j]:
                check[j] = check[k] + 1
                break

        else:
            break

    for j in range(i-1,-1,-1):
        for k in range(i,j,-1):
            if d[k] - check[k] <= d[j]:
                check[j] = check[k] + 1
                break

        else:
            break

    cnt = sum(map(bool,check))
    res = max(res,cnt)

print(res)