l = int(input())
n = int(input())
val = -1
idx = None
line = [0]*(l+1)
for i in range(1,n+1):
    p,k = map(int,input().split())
    if val < k-p+1:
        val = k-p+1
        idx = i

    for j in range(p,k+1):
        if not line[j]:
            line[j] = i

cnt = [0]*(n+1)
for i in line:
    cnt[i] += 1

val2 = -1
idx2 = None
for i in range(1,n+1):
    if val2 < cnt[i]:
        val2 = cnt[i]
        idx2 = i

print(idx)
print(idx2)