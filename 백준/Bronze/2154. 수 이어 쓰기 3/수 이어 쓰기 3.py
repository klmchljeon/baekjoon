n = int(input())
d = [str(i) for i in range(1,n+1)]
st = ''.join(d)

print(st.find(str(n))+1)