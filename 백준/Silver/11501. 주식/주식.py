#주식
t = int(input())
for case in range(t):
    n = int(input())
    d = list(map(int,input().split()))
    st = []
    for i in range(n):
        while st and st[-1][1] <= d[i]:
            st.pop()

        st.append((i,d[i]))

    st = st[::-1]

    res = 0
    for i in range(n):
        res += st[-1][1] - d[i]

        if st[-1][0] == i:
            st.pop()

    print(res)