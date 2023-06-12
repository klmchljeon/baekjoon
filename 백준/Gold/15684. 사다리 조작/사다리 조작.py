#사다리 조작 28:33
def sim():
    for i in range(1,n+1):
        idx = i
        for j in range(1,h+1):
            idx += d[j][idx]

        if idx != i:
            return 0
            
    return 1

def dfs(l):
    if len(s) == l:
        tmp.append(tuple(map(conv,s)))
        return 
    
    for i in range(can):
        if not s or s[-1]<i:
            s.append(i)
            dfs(l)
            s.pop()

    return 

conv = lambda x:(x//(n-1)+1, x%(n-1)+1)

n,m,h = map(int,input().split())
d = [[0]*(n+1) for _ in range(h+1)]

for _ in range(m):
    a,b = map(int,input().split())
    d[a][b] = 1
    d[a][b+1] = -1

if sim():
    print(0)
    exit()

can = h*(n-1)
s = []
for i in range(1,4):
    tmp = []
    dfs(i)

    for c in tmp:
        flag = False

        st = set()
        for x,y in c:
            if d[x][y]!=0 or d[x][y+1]!=0:
                flag = True

            st.add((x,y))
            st.add((x,y+1))    

        if flag or len(st)!=len(c)*2: continue

        for x,y in c:
            d[x][y] = 1
            d[x][y+1] = -1

        if sim():
            print(i)
            exit()

        for x,y in c:
            d[x][y] = 0
            d[x][y+1] = 0

print(-1)