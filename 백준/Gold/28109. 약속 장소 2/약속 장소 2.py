alpha = [chr(i+ord('A')) for i in range(26)]
dic = dict(zip(alpha,range(26)))

n,k = map(int,input().split())
st = [dic[i] for i in input()]

cnt = 0
for i in range(n):
    tmp = st[i]
    for j in range(tmp):
        st[i] = j
        cnt += 1
        if cnt == k:
            print(''.join([alpha[idx] for idx in st]))
            exit()

    st[i] = tmp

cnt += 1
if cnt == k:
    print(''.join([alpha[idx] for idx in st]))
    exit()

for i in range(n)[::-1]:
    tmp = st[i]
    for j in range(tmp+1,26):
        st[i] = j
        cnt += 1
        if cnt == k:
            print(''.join([alpha[idx] for idx in st]))
            exit()

    st[i] = tmp

print(-1)