n = int(input())
st = set()
for _ in range(n):
    lst = input().split()
    m = len(lst)
    for i in range(m):
        if not lst[i][0].upper() in st:
            st.add(lst[i][0].upper())
            lst[i] = f'[{lst[i][0]}]{lst[i][1:]}'
            break

    else:
        for i in range(m):
            for j in range(len(lst[i])):
                if not lst[i][j].upper() in st:
                    st.add(lst[i][j].upper())
                    lst[i] = f'{lst[i][:j]}[{lst[i][j]}]{lst[i][j+1:]}'
                    break

            else:
                continue

            break

    print(*lst)