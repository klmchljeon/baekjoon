#민균이의 비밀번호
n = int(input())
st = set()
for _ in range(n):
    st.add(input())
    
for i in st:
    if i[::-1] in st:
        print(len(i),i[len(i)//2])
        exit()