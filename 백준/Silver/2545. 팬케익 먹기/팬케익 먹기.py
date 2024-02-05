n = int(input())
for case in range(n):
    input()
    a,b,c,d = map(int,input().split())
    a,b,c = sorted([a,b,c])
    if c-b >= d:
        c -= d

    else:
        d -= c-b
        c = b

        if (b-a)*2 >= d:
            b -= d//2
            c -= d//2 + d%2

        else:
            tmp = a+b+c - d
            a = tmp//3
            b = tmp//3 + (tmp%3>=1)
            c = tmp//3 + (tmp%3>=2)

    res = a*b*c
    print(res)