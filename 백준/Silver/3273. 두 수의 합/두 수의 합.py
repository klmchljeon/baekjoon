n = int(input())
lst = list(map(int,input().split()))
x = int(input())

lst.sort()

e = n-1
cnt = 0
for s in range(n):
    while lst[s]+lst[e]>x and s+1<e:
        e -= 1

    if lst[s] + lst[e] == x:
        cnt += 1

print(cnt)