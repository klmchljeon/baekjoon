dic = dict(zip('RGB',range(3)))

n = int(input())
st = input()
lst = [dic[i] for i in st]

res = int(1e9)
for p in (0,1,2):
    tmp = lst[:]
    cnt = 0
    for i in range(n-2):
        while tmp[i] != p:
            for j in range(i,i+3):
                tmp[j] = (tmp[j] + 1)%3

            cnt += 1

    if tmp[n-2] == tmp[n-1] and tmp[n-1] == p:
        res = min(res,cnt)

print(res if res!=int(1e9) else -1)