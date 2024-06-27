d = [-1]*8
for i in range(8):
    st = input()
    for j in range(8):
        if st[j] == '*':
            d[i] = j

st1 = set([d[i]-i for i in range(8)])
st2 = set([d[i]+i for i in range(8)])

flag1 = not -1 in d and len(set(d))==8
flag2 = len(st1)==8 and len(st2)==8

res = 'valid' if flag1 and flag2 else 'invalid'
print(res)