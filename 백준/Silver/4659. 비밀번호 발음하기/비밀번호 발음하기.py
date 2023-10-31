t = 'aeiou'
p = 'eo'

while True:
    st = input()
    if st == 'end': break
    n = len(st)

    flag = False
    for i in st:
        if i in t:
            break

    else:
        flag = True

    for i in range(n-2):
        a,b,c = st[i:i+3]
        if a in t and b in t and c in t:
            flag = True
            break

        elif not (a in t or b in t or c in t):
            flag = True
            break

    for i in range(n-1):
        a,b = st[i:i+2]
        if a==b and not a in p:
            flag = True
        
    res = 'not ' if flag else ''
    print(f'<{st}> is {res}acceptable.')