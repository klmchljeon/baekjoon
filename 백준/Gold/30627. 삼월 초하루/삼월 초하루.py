from collections import deque
m = 20

n = int(input())
t1,t2 = map(int,input().split())

p = (-1,t1//5,t2//5)
lst = list(map(int,input().split()))

prev = [[[[None]*(m+2) for _ in range(m+2)] for _ in range(m+2)] for _ in range(2)]
visited = [[[[False]*(m+2) for _ in range(m+2)] for _ in range(m+2)] for _ in range(2)]
visited[0][m][m][-1] = True

queue = deque([((m,m),3,0)])
while queue:
    w,idx,s = queue.popleft()
    a,b = w
    if idx == 1:
        if a > 0 and visited[s][a-1][-1][b] == False:
            visited[s][a-1][-1][b] = True
            prev[s][a-1][-1][b] = ((-1,a,b),(2,1),s)
            queue.append(((a-1,b),2,s))

        if b > 0 and visited[s^1][b-1][a][-1] == False:
            visited[s^1][b-1][a][-1] = True
            prev[s^1][b-1][a][-1] = ((-1,a,b),(3,1),s^1)
            queue.append(((b-1,a),3,s^1))

    elif idx == 2:
        if a > 0 and visited[s][-1][a-1][b] == False:
            visited[s][-1][a-1][b] = True
            prev[s][-1][a-1][b] = ((a,-1,b),(1,2),s)
            queue.append(((a-1,b),1,s))

        if b > 0 and visited[s][a][b-1][-1] == False:
            visited[s][a][b-1][-1] = True
            prev[s][a][b-1][-1] = ((a,-1,b),(3,2),s)
            queue.append(((a,b-1),3,s))

    elif idx == 3:
        if a > 0 and visited[s^1][-1][b][a-1] == False:
            visited[s^1][-1][b][a-1] = True
            prev[s^1][-1][b][a-1] = ((a,b,-1),(1,3),s^1)
            queue.append(((b,a-1),1,s^1))

        if b > 0 and visited[s][a][-1][b-1] == False:
            visited[s][a][-1][b-1] = True
            prev[s][a][-1][b-1] = ((a,b,-1),(2,3),s)
            queue.append(((a,b-1),2,s))

rank = [0,0,0]
for i in range(3):
    rank[i] = p[lst[i]]

s = lst.index(1) > lst.index(2)

i1,i2,i3 = rank
if not visited[s][i1][i2][i3]:
    print(-1)
    exit()

res = []
tmp = prev[s][i1][i2][i3]
while tmp != None:
    loc,move,_ = tmp
    res.append(move)
    s ^= (move in ((1,3),(3,1)))

    i1,i2,i3 = loc
    tmp = prev[s][i1][i2][i3]

print(len(res))
for i in res[::-1]:
    print(*i)