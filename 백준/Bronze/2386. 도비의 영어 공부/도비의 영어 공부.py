while True:
    a = input()
    if a[0] == '#': break

    cnt = 0
    for i in a[1:].lower():
        cnt += i == a[0]

    print(a[0],cnt)