#ROT13
st = list(input())
for i in range(len(st)):
    if 'a' <= st[i] <= 'z':
        tmp = ord(st[i])+13
        if tmp > ord('z'):
            tmp -= 26

        st[i] = chr(tmp)

    if 'A' <= st[i] <= 'Z':
        tmp = ord(st[i])+13
        if tmp > ord('Z'):
            tmp -= 26

        st[i] = chr(tmp)

print(''.join(st))