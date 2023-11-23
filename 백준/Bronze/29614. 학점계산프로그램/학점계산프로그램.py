alpha = 'ABCDF'
dic = dict(zip(alpha,range(4,-1,-1)))
dic['+'] = 0.5

st = input()
res = 0
cnt = 0
for i in st:
    res += dic[i]
    cnt += i!='+'

print(res/cnt)