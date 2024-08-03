n = int(input())
ans = input().split()
lst = input().split()

st = set(ans)
dic = dict(zip(lst,range(n)))
cnt = 0
for i in range(n-1):
    st.remove(ans[i])
    if not ans[i] in dic:
        continue

    idx = dic[ans[i]] + 1
    for j in range(idx,n):
        if lst[j] in st:
            cnt += 1

print(cnt,n*(n-1)//2,sep='/')