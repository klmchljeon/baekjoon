import sys
input = sys.stdin.readline

def cal(tmp):
    idx = [d[i][1] for i in tmp]
    x = [0,40001]
    y = [0,40001]
    for loc,i in lst:
        if i in idx: continue

        cx,cy = loc
        x = [max(x[0],cx), min(x[1],cx)]
        y = [max(y[0],cy), min(y[1],cy)]

    return (x[1]-x[0])*(y[1]-y[0])

n = int(input())
lst = []
for i in range(n):
    x,y = map(int,input().split())
    lst.append(((x,y),i))

st = set()
lst.sort(key = lambda x:x[0][0])
st.update(lst[:3] + lst[-3:])

lst.sort(key = lambda x:x[0][1])
st.update(lst[:3] + lst[-3:])

d = list(st)
m = len(d)

res = 40000**2
for i in range(m-2):
    for j in range(i+1,m-1):
        for k in range(j+1,m):
            res = min(res,cal((i,j,k)))

print(res)