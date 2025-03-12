t = int(input())
for case in range(t):
    st = input()
    n = len(st)
    print(min(n-st.count('a'),st.count('a')))