n,m = map(int,input().split())
lst = list(map(int,input().split()))

e = 0
sum_ = 0
cnt = 0
for s in range(n):
    while sum_<m and e<n:
        sum_ += lst[e]
        e += 1

    if sum_ == m:
        cnt += 1

    sum_ -= lst[s]

print(cnt)