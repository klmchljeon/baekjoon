t = int(input())
for case in range(t):
    n = int(input())
    dic1 = dict()
    dic2 = dict()
    for i in range(n):
        a = input()
        b = input()
        dic1[a] = b
        dic2[b] = a

    tmp = b
    while tmp in dic2:
        tmp = dic2[tmp]

    res = []
    for i in range(n):
        res.append('-'.join((tmp,dic1[tmp])))
        tmp = None if not tmp in dic1 else dic1[tmp]

    print(f'Case #{case+1}:',*res,sep=' ')
