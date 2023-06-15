#게임을 만든 동준이
n = int(input())
d = [int(input()) for _ in range(n)]
d = d[::-1]

prev = d[0]+1
cnt = 0
for i in range(n):
    if d[i] >= prev:
        cnt += d[i]-prev+1
        d[i] = prev-1

    prev = d[i]

print(cnt)