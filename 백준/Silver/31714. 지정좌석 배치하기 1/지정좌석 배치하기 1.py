n,m,d = map(int,input().split())
flag = True
prev = list(map(int,input().split()))
prev.sort()
for _ in range(n-1):
    lst = list(map(int,input().split()))
    lst.sort()
    for j in range(m):
        flag &= lst[j]+d > prev[j]

    prev = lst[:]

print('YES' if flag else 'NO')