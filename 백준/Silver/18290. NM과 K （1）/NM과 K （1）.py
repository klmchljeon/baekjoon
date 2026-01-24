dx = (-1,1,0,0)
dy = (0,0,-1,1)

def bt():
    if len(s) == k:
        bt_lst.append(tuple(s))
        return
    
    for i in range(lena):
        if not s or s[-1] < i:
            s.append(i)
            bt()
            s.pop()

    return 

def check(idx):
    st = set()
    for i in idx:
        x,y = arr[i][1]

        if (x,y) in st:
            return False

        for j in range(4):
            nx = x + dx[j]
            ny = y + dy[j]

            st.add((nx,ny))

    return True

n,m,k = map(int,input().split())
lst = []
for i in range(n):
    tmp = list(map(int,input().split()))
    lst.append(tmp)

arr = []
for i in range(n):
    for j in range(m):
        arr.append((lst[i][j],(i,j)))

arr.sort(key = lambda x:-x[0])

arr = arr[:20]
lena = len(arr)

bt_lst = []
s = []

bt()

res = -int(1e5)
for p in bt_lst:
    if not check(p): continue

    sum_ = 0
    for i in p:
        sum_ += arr[i][0]

    res = max(res,sum_)

print(res)