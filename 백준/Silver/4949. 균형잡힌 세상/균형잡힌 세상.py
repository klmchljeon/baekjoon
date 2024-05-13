#균형잡힌 세상
import sys
input = sys.stdin.readline

ket = set(['(',')','[',']'])

while True:
    st = input().rstrip()
    if st == '.':
        exit(0)

    d = [None]
    result = 'yes'
    for i in st:
        if not i in ket:
            continue

        if i == '(' or i == '[':
            d.append(i)

        else:
            if d[-1] == '(' and i == ')':
                d.pop()
            elif d[-1] == '[' and i == ']':
                d.pop()
            else:
                result = 'no'
                break

    if len(d) != 1:
        result = 'no'

    print(result)