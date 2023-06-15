#유학 금지
a = 'CAMBRIDGE'
st = list(input())
for i in range(len(st)):
    if st[i] in a:
        st[i] = ''

print(''.join(st))