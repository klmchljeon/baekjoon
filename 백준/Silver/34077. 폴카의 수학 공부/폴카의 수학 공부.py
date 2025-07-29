import sys
input = sys.stdin.readline

t = int(input())
for case in range(t):
    n = int(input())
    st = list(input().rstrip())
    while len(st) >= 2:
        if st[-1] == '0':
            st.pop()
            st.pop()
        else:
            break

    flag = not '-' in st[:-3]
    print('YES' if flag else 'NO')