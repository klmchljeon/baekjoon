def find(loc,di):
    x,y = loc
    for i in range(len(st)):
        nx = x + i*dx[di]
        ny = y + i*dy[di]

        if not (0<=nx<n and 0<=ny<m): 
            return False

        if d[nx][ny] != st[i]:
            return False
        
    return True

def main():
    for i in range(n):
        for j in range(m):
            for k in range(8):
                if find((i,j),k):
                    return True
                
    return False

dx = (-1,1,0,0,-1,-1,1,1)
dy = (0,0,-1,1,-1,1,-1,1)

st = input()
n,m = map(int,input().split())
d = [input() for _ in range(n)]
print(int(main()))