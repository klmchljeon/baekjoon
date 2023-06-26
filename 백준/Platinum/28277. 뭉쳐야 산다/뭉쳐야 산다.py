import sys
input = sys.stdin.readline

def insert(a,b):
    ia,ib = idx[a],idx[b]

    if len(st[ia]) >= len(st[ib]):
        for i in st[ib]:
            st[ia].add(i)

        st[ib].clear()

    else:
        for i in st[ia]:
            st[ib].add(i)

        st[ia].clear()

        idx[a],idx[b] = ib,ia

    return 

n,q = map(int,input().split())

idx = [i-1 for i in range(n+1)]
st = [] 

for _ in range(n):
    _,*lst = map(int,input().split())
    st.append(set(lst))

for query in range(q):
    m,*order = map(int,input().split())
    if m==1:
        insert(*order)
    else:
        print(len(st[idx[order[0]]]))