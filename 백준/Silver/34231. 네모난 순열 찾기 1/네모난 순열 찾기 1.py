n = int(input())
lst = []
for _ in range(n):
    tmp = list(map(int,input().split()))
    lst.append(tmp)

cnt = 0
for r1 in range(n):
    for r2 in range(r1,n):
        for c1 in range(n):
            for c2 in range(c1,n):
                m = (r2-r1+1)*(c2-c1+1)
                v = [0]*(m+1)
                flag = True
                for i in range(r1,r2+1):
                    for j in range(c1,c2+1):
                        if lst[i][j] < m+1 and v[lst[i][j]] == 0:
                            v[lst[i][j]] = 1

                        else:
                            flag = False
                            break

                cnt += flag

print(cnt)