#머리 톡톡
import sys
input = sys.stdin.readline
t = 1000000

n = int(input())
d = [int(input()) for _ in range(n)]

lst = [0]*(t+1)
for i in d:
    lst[i] += 1

cnt = [0]*(t+1)
for i in range(1,t+1):
    if lst[i]:
        cnt[i] += lst[i]-1
        for j in range(i+i,t+1,i):
            cnt[j] += lst[i]

for i in d:
    print(cnt[i])