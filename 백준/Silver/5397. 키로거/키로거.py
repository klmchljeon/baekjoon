#키로거
t = int(input())
for case in range(t):
    st = input()

    s1 = []
    s2 = []
    for i in st:
        if i=='<':
            if s1:
                s2.append(s1.pop())

        elif i=='>':
            if s2:
                s1.append(s2.pop())

        elif i=='-':
            if s1:
                s1.pop()

        else:
            s1.append(i)

    print(*s1,*s2[::-1],sep='')