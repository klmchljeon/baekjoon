import sys
input = sys.stdin.readline

day = [0,31,28,31,30,31,30,31,31,30,31,30,31]

def check(a):
    if a%4 == 0:
        if a%100 == 0:
            if a%400 == 0:
                return 1
            else:
                return 0
        else:
            return 1
    else:
        return 0

while True:
    lst = input().rstrip().split('/')
    if lst[0] == 'end': break

    if len(lst) != 2:
        print('invalid')
        continue

    if len(lst[0]) != 6:
        print('invalid')
        continue

    a,b = lst
    y,m,d = map(int,(a[:2],a[2:4],a[4:]))

    w = m > 50
    if w:
        m -= 50

    if not (1 <= m <= 12):
        print('invalid')
        continue

    if check(y) and m == 2:
        tmp = day[m] + 1
    else:
        tmp = day[m]

    if not (1 <= d <= tmp):
        print('invalid')
        continue

    if 10 <= y <= 19:
        print('invalid')
        continue

    if 20 <= y <= 53:
        if len(b) != 3:
            print('invalid')
            continue

    else:
        if len(b) != 4:
            print('invalid')
            continue

        n = int(a+b)
        if n%11 != 0:
            print('invalid')
            continue

    print('girl' if w else 'boy')