n,k = map(int,input().split())
tmp = [0]*n
a = list(map(int,input().split()))
for i in a:
    tmp[i] = 1

prefix = [0]
for i in tmp:
    prefix.append(prefix[-1]+i)

lst = list(map(int,input().split()))
s = 0 #0개수
p = 0 #소등 못한 방의 수
for i in range(n):
    if lst[i] == 0:
        s += 1
        continue

    if prefix[i-p+1] - prefix[s] == 0:
        p += 1

print(p)