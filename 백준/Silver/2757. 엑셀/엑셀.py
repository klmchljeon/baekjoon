alpha = [chr(i + ord('A')) for i in range(26)]

while True:
    tmp = input()
    r,c = map(int,tmp[1:].split('C'))
    if r==0 and c==0:
        break

    res = []
    while c:
        c -= 1
        c,mod = divmod(c,26)
        res.append(alpha[mod])

    res = res[::-1]

    st = f"{''.join(res)}{r}"
    print(st)
