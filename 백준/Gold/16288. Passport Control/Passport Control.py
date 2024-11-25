n,k = map(int,input().split())
lst = list(map(int,input().split()))

cnt = 0
while lst:
    idx = -1
    tmp = []
    while idx+1 < len(lst):
        cur = min(lst[idx+1:])
        idx = lst.index(cur)
        tmp.append(idx)

    while tmp:
        lst.pop(tmp.pop())

    cnt += 1

print('YES' if cnt <= k else 'NO')