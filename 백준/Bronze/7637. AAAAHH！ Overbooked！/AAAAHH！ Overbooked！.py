conv = lambda x:60*x[0]+x[1]
r = lambda x:conv(list(map(int,x.split(':'))))

while True:
    n = int(input())
    if not n: break

    lst = [0]*(24*60)
    flag = True
    for i in range(n):
        a,b = input().split('-')
        for idx in range(r(a),r(b)):
            if not lst[idx]:
                lst[idx] = 1
            else:
                flag = False

    if flag:
        print('no conflict')
    else:
        print('conflict')