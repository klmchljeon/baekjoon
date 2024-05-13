lst = ['EI','SN','TF','JP']

st = input()
res = ''
for i in range(4):
    for j in lst[i]:
        if st[i] != j:
            res += j

print(res)