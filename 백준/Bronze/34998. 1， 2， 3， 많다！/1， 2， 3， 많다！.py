n = int(input())
for case in range(n):
    x = int(input())
    lst = input().split('+')
    res = 0
    for i in lst:
        if i.strip() == '!':
            res += 10

        else:
            res += int(i)

    print(res if res < 10 else '!')