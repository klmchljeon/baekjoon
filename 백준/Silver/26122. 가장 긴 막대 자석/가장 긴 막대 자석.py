k = int(input())
st = input()

res = 0

for c in 'NS':
    cnt1 = 0
    tmp = 0
    cnt2 = 0
    for i in st:
        if i == c:
            cnt1 += 1
            cnt2 = 0
            tmp = 0

        else:
            if tmp == 0:
                tmp = cnt1
                cnt1 = 0

            cnt2 += 1
            res = max(res,min(tmp,cnt2)*2)

print(res)