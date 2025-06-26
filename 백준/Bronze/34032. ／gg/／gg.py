n = int(input())
st = input()
cnt = st.count('O')
print('Yes' if cnt*2 >= n else 'No')