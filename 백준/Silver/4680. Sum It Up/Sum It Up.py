while True:
    s,n,*lst = map(int,input().split())
    if s==0 and n==0: break

    st = set()

    print(f"Sums of {s}:")
    for i in range(1<<n):
        tmp = []
        p = 0
        for j in range(n):
            if i&(1<<j):
                tmp.append(lst[j])
                p += lst[j]

        if p == s:
            st.add(tuple(tmp))

    if not st:
        print("NONE")
        continue

    for i in sorted(st)[::-1]:
        print(*i, sep = '+')