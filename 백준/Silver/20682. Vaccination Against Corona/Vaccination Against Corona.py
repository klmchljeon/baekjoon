n,l = map(int,input().split())
lst = list(map(int,input().split()))
lst.sort()

cnt = 0
prev = lst[0]
for i in range(1,n):
    if lst[i] - prev >= l:
        prev = lst[i]

    else:
        cnt += 1

print(cnt)