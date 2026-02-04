t = int(input())
for case in range(t):
    n = int(input())
    lst = input().split()
    for i in range(n):
        a,b = lst[i].split('.')
        b += (3-len(b))*'0'
        lst[i] = 2*int(a+b)

    lst.sort()
    while len(lst) > 1:
        p = lst.pop()
        if p <= sum(lst):
            print('YES')
            break

    else:
        print('NO')