n = int(input())
st = set()
for i in range(n):
    s = ''.join(sorted(input()))
    st.add(s)

print(len(st))