t = int(input())
for case in range(t):
    st = input()
    n = int(st) + int(st[::-1])
    tmp = str(n)
    if tmp == tmp[::-1]:
        print('YES')
    else:
        print('NO')