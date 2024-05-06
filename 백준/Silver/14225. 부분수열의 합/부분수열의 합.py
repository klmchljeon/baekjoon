n = int(input())
d = list(map(int,input().split()))

st = set()
for v in range(1<<n):
    tmp = 0
    for i in range(n):
        if v&(1<<i):
            tmp += d[i]

    st.add(tmp)

res = 0
while res in st:
    res += 1

print(res)