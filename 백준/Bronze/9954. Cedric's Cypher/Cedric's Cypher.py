while True:
    st = input()
    if st == '#': break

    m = ord('A') - ord(st[-1])

    res = ''
    for i in st[:-1]:
        if 'a' <= i <= 'z':
            j = ord(i) + m
            if j < ord('a'):
                j += 26

        elif 'A' <= i <= 'Z':
            j = ord(i) + m
            if j < ord('A'):
                j += 26

        else:
            j = ord(i)

        res += chr(j)

    print(res)