#오르막길
n = int(input())
d = list(map(int,input().split()))

prev = [d[0],0]
res = 0

for i in d:
    if prev[0] < i:
        prev[1] += i-prev[0]

    else:
        res = max(res,prev[1])
        prev[1] = 0

    prev[0] = i

res = max(res,prev[1])
print(res)