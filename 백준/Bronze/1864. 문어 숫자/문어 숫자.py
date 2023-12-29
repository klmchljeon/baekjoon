st = '/-\(@?>&%'
dic = dict(zip(st,range(-1,8)))

while True:
    a = input()
    if a == '#':
        break

    cnt = 0
    res = 0
    for i in a[::-1]:
        res += dic[i]*8**cnt
        cnt += 1

    print(res)