x,k = map(int,input().split())
lst = list(map(int,input().split()))
cnt = [0]*(k+1)
for i in range(x):
    cnt[lst[i]] += 1

res = 0
for i in range(x,2*x):
    res += x - cnt[lst[i]]

print(res)