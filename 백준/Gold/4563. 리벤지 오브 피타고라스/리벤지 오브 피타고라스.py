while True:
    a = int(input())
    if a == 0: break

    cnt = 0
    for i in range(1,a):
        if a**2 % i != 0: continue

        j = a**2 // i

        c2 = (j+i)
        b2 = (j-i)

        if c2%2==0 and b2%2==0 and b2//2 > a:
            cnt += 1

    print(cnt)