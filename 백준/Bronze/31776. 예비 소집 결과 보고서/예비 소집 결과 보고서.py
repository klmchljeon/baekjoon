n = int(input())
cnt = 0
for _ in range(n):
    d = list(map(int,input().split()))
    
    t = -1
    flag = False
    flag2 = False
    for i in d:
        if flag and i != -1:
            break

        if i == -1:
            flag = True
        else:
            flag2 = True

        if not flag and t > i:
            break

        t = i

    else:
        cnt += flag2

print(cnt)