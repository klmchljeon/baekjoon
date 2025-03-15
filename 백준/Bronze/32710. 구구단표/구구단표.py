st = set()
for i in range(2,10):
    for j in range(1,10):
        st.add(i)
        st.add(j)
        st.add(i*j)

n = int(input())
print(int(n in st))