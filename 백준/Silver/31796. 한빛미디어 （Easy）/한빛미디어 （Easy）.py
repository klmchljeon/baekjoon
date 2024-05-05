n = int(input())
lst = list(map(int,input().split()))
lst.sort()

cnt = 1
m = lst[0]
for i in lst:
    if m*2 <= i:
        cnt += 1
        m = i

print(cnt)