st = list(input())[::-1]

i = 1
while True:
    d = list(str(i))[::-1]
    while st and d:
        if d[-1] == st[-1]:
            d.pop()
            st.pop()
        else:
            d.pop()

    if not st:
        print(i)
        break

    i += 1