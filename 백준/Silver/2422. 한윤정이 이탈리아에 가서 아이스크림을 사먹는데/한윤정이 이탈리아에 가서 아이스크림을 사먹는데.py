import sys
input = sys.stdin.readline

n,m = map(int,input().split())
st = set()
for _ in range(m):
    a,b = map(int,input().split())
    if a > b: a,b = b,a

    st.add((a,b))

cnt = 0
for i in range(1,n-1):
    for j in range(i+1,n):
        for k in range(j+1,n+1):
            f1 = not (i,j) in st
            f2 = not (i,k) in st
            f3 = not (j,k) in st

            cnt += f1 and f2 and f3

print(cnt)