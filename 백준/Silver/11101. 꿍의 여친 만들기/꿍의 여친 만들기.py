t = int(input())
for case in range(t):
    tmp = input().split(',')
    dic = dict()
    for i in tmp:
        a,b = i.split(':')
        dic[a] = int(b)

    res = 1000

    p = input().split('|')
    for i in p:
        lst = [dic[j] for j in i.split('&')]
        m = max(lst)
        res = min(res,m)

    print(res)