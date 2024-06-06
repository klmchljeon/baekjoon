t = int(input())
for case in range(t):
    st = input()
    p = None
    for i in st:
        if '0' <= i <= '9':
            continue

        p = i
        break

    lst = list(map(int,st.split(p)))

    if p == '+':
        lst.append(lst[0]+lst[1])

    elif p == '-':
        lst.append(lst[0]-lst[1])

    else:
        tmp = lst[1]
        while tmp > 0:
            lst.append(lst[0]*(tmp%10))
            tmp //= 10

        if len(lst) > 3:
            lst.append(lst[0]*lst[1])

    lst = list(map(str,lst))

    lst[1] = p + lst[1]

    line1 = max(len(lst[1]),len(lst[2]))*'-'
    lst.insert(2,line1)

    s = 0
    for i in range(3,len(lst)-1):
        lst[i] += ' '*s
        s += 1 

    if len(lst) > 4:
        line2 = max(len(lst[-1]),len(lst[-2]))*'-'
        lst.insert(-1,line2)

    n = max(map(len,lst))
    
    for i in range(len(lst)):
        lst[i] = (n-len(lst[i]))*' ' + lst[i]

    for i in lst:
        print(i.rstrip())
    if case != t-1:
        print()