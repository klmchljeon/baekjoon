#크로스워드
r,c = map(int,input().split())
d = [list(input()) for _ in range(r)]

st = set()
for i in range(r):
    word = ''
    for j in range(c):
        if d[i][j] == '#':
            if len(word) >= 2:
                st.add(word)

            word = ''

        else:
            word += d[i][j]

    if len(word) >= 2:
        st.add(word)

for j in range(c):
    word = ''
    for i in range(r):
        if d[i][j] == '#':
            if len(word) >= 2:
                st.add(word)

            word = ''
            
        else:
            word += d[i][j]

    if len(word) >= 2:
        st.add(word)

print(sorted(st)[0])