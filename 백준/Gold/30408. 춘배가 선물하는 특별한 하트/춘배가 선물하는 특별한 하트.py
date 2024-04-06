n,m = map(int,input().split())
stack = [n]
st = set([n])
while stack:
    x = stack.pop()
    if x&1:
        a,b = x//2,x//2+1
        if not a in st:
            st.add(a)
            stack.append(a)

        if not b in st:
            st.add(b)
            stack.append(b)

    else:
        a = x//2
        if not a in st:
            st.add(a)
            stack.append(a)

print('YES' if m in st else 'NO')