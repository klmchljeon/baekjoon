#방 배정
n,k = map(int,input().split())
d = [[0]*6 for _ in range(2)]

for _ in range(n):
    s,y = map(int,input().split())
    d[s][y-1] += 1

cnt = 0
for i in range(2):
    for j in range(6):
        cnt += d[i][j]//k + (d[i][j]%k!=0)

print(cnt)