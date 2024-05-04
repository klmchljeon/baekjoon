max_ = int(1e18)

n = int(input())
a = list(map(int,input().split()))
lst = []
for i in a:
    lst.append(i%2)

ans = max_
for tar in (0,1):
    cnt = 0
    res = 0
    for i in range(n):
        if lst[i] != tar:
            continue

        res += i-cnt
        cnt += 1

    ans = min(ans,res)

print(ans)