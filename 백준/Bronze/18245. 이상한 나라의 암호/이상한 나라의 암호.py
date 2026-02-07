idx = 1
while True:
    st = input()
    if st == 'Was it a cat I saw?': break

    ans = ''
    for i in range(0,len(st),idx+1):
        ans += st[i]

    print(ans)

    idx += 1