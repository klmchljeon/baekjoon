a = 'aeios'
b = [4,3,1,0,5]
dic = dict(zip(a,map(str,b)))

st = list(input())

for i in range(len(st)):
    if st[i] in dic:
        st[i] = dic[st[i]]

print(''.join(st))