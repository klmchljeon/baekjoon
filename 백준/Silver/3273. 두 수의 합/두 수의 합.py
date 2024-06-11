max_ = 2000000

n = int(input())
lst = list(map(int,input().split()))
x = int(input())

res = 0

#cnt[i] : i가 이전까지 등장한 횟수
cnt = [0]*(max_+1)
for i in range(n):
    res += cnt[x-lst[i]]
    cnt[lst[i]] += 1

print(res)