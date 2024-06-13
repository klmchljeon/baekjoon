import sys
input = sys.stdin.readline

n = int(input())
d = [int(input()) for _ in range(n)]

cnt = [0]*21
for i in d:
    cnt[i] += 1

for i in range(20,0,-1):
    if cnt[i] >= 2:
        cnt[i-1] += cnt[i]//2
        cnt[i] -= 2*cnt[i]//2

if cnt[0]:
    print('A')
else:
    print('B')