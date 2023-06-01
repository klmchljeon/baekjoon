while True:
    b,n = map(int,input().split())
    if not b: break

    res = [1,b-1]
    a = 1
    while True:
        if (a-1)**n > b:
            break

        if res[1] > abs(a**n-b):
            res = [a,abs(a**n-b)]
        
        a += 1

    print(res[0])