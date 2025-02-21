r = 1
res = int(input())
num = None
while True:
    if r:
        p = input()
        if p == '=':
            print(res)
            break

    else:
        num = int(input())
        if p == '+':
            res += num
        elif p == '-':
            res -= num
        elif p == '*':
            res *= num
        else:
            res //= num

    r ^= 1