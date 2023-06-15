#폴리오미노
st = list(input().split('.'))
for i in range(len(st)):
    if not 'X' in st[i]: continue

    if len(st[i])&1:
        print(-1)
        exit()

    div,mod = divmod(len(st[i]),4)
    tmp = 'A'*4*div + 'B'*mod
    st[i] = tmp

print('.'.join(st))