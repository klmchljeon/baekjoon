t = int(input())
for case in range(t):
    st = input()
    a = 0
    b = 0
    num = None
    for i in st:
        if i == '!':
            if num == None:
                a += 1
            else:
                b += 1

        else:
            num = int(i)

    if b:
        num = 1

    num ^= a%2
    print(num)