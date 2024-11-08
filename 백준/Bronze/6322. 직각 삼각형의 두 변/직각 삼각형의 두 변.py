cnt = 0
while True:
    a,b,c = map(int,input().split())
    if a==0: break
    if cnt != 0:
        print()

    if a == -1:
        tmp = c**2 - b**2
        if tmp <= 0:
            res = "Impossible."
        else:
            res = f"a = {tmp**0.5:.3f}"

    elif b == -1:
        tmp = c**2 - a**2
        if tmp <= 0:
            res = "Impossible."
        else:
            res = f"b = {tmp**0.5:.3f}"

    else:
        res = f"c = {(a**2 + b**2)**0.5:.3f}"

    cnt += 1
    print(f"Triangle #{cnt}")
    print(res)