n = int(input())
st = input()

for i in range(1,n+1):
    st1 = st[:i]
    st2 = st[n-i:]
    cnt = 0
    for j in range(i):
        cnt += st1[j]!=st2[j]

    if cnt == 1:
        print('YES')
        break

else:
    print('NO')