t = int(input())
for case in range(t):
    name,*d = input().split()
    a,b,c = map(int,d)

    flag = True
    flag &= a+b+c >= 55
    for i in zip((a,b,c),(35,25,40)):
        flag &= i[0] >= i[1]*3/10

    res = 'PASS' if flag else 'FAIL'
    print(name,a+b+c,res)