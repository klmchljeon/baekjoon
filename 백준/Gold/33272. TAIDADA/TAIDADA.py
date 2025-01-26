n,m,k = map(int,input().split())
st = set()
res = []
for i in range(1,m+1):
    if not i in st:
        res.append(i)
        st.add(k^i)
        if len(res) == n:
            print(*res)
            break

else:
    print(-1)