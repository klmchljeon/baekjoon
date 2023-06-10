#주사위 굴리기
def move(dir):
    fir = dice[0]
    for i in range(3):
        tmp = dice[conv[dir][i+1]]
        dice[conv[dir][i]] = tmp

    dice[conv[dir][3]] = fir
    return 

dx = (None,0,0,-1,1)
dy = (None,1,-1,0,0)

conv = (
    None,
    (0,2,5,3),
    (0,3,5,2),
    (0,1,5,4),
    (0,4,5,1)
)

n,m,x,y,k = map(int,input().split())
d = [list(map(int,input().split())) for _ in range(n)]
q = list(map(int,input().split()))

dice = [0,0,0,0,0,0]

for i in q:
    nx = x + dx[i]
    ny = y + dy[i]
    if not (0<=nx<n and 0<=ny<m): continue

    x = nx
    y = ny
    move(i)
    
    if d[x][y] == 0:
        d[x][y] = dice[0]

    else:
        dice[0] = d[x][y]
        d[x][y] = 0

    print(dice[5])