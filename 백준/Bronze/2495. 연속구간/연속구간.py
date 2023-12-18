for _ in range(3):
    st = input()
    res = 1
    for i in range(10):
        for j in range(2,9):
            if str(i)*j in st:
                res = max(res,j)

    print(res)