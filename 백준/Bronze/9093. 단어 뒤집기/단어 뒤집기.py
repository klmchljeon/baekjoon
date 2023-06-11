#단어 뒤집기
n = int(input())
for _ in range(n):
    st = input().split()
    for i in range(len(st)):
        st[i] = st[i][::-1]

    print(*st)