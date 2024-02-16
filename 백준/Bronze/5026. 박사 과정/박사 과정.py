n = int(input())
for case in range(n):
    st = input()
    if st == 'P=NP':
        print('skipped')
    else:
        print(sum(map(int,st.split('+'))))