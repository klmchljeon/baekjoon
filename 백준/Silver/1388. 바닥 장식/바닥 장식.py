n,m = map(int,input().split())
st = [input() for _ in range(n)]
cnt = 0
for i in range(n):
    prev = ''
    for j in range(m):
        cnt += prev != '-' and st[i][j] == '-'

        prev = st[i][j]

for j in range(m):
    prev = ''
    for i in range(n):
        cnt += prev != '|' and st[i][j] == '|'

        prev = st[i][j]
    
print(cnt)