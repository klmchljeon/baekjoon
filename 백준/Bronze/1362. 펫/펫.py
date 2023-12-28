case = 0
while True:
    o,w = map(int,input().split())
    if not o: break

    die = False
    case += 1

    while True:
        order,n = input().split()
        if order == '#':
            print(case,end = ' ')
            if die:
                print('RIP')
            elif o < w*2 < o*4:
                print(':-)')
            else:
                print(':-(')
            break

        n = int(n)
        if order == 'E':
            w -= n
            if w <= 0:
                die = True

        if order == 'F':
            w += n