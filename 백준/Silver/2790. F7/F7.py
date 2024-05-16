import sys
input = sys.stdin.readline

n = int(input())
d = [int(input()) for _ in range(n)]
d.sort(reverse = True)

cnt = 0
max_ = d[0]+1
for i in range(n):
    if d[i]+n >= max_:
        cnt += 1

    max_ = max(max_,d[i]+i+1)

print(cnt)