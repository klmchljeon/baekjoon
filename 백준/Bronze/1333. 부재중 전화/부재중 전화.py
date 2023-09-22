max_ = 10000

n,l,d = map(int,input().split())
lst = [0]*(max_+1)

idx = 0
for i in range(n):
    for j in range(l):
        lst[idx] = 1
        idx += 1

    idx += 5

idx = 0
while idx <= max_:
    if not lst[idx]:
        break

    idx += d

print(idx)