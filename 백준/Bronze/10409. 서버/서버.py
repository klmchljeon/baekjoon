n,t = map(int,input().split())
d = list(map(int,input().split()))

cnt = 0
tmp = 0
for i in d:
    if tmp + i <= t:
        tmp += i
        cnt += 1

    else:
        break

print(cnt)