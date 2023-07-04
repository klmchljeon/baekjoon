n = int(input())

a = '2023'
cnt = 0
for p in range(2022,n+1):
    st = str(p)

    idx = 0
    for i in st:
        if i == a[idx]:
            idx += 1

        if idx == 4:
            cnt += 1
            break

print(cnt)