n = int(input())
st = set()

stack = []
for i in range(n):
    a = int(input())
    if not a in st:
        st.add(a)
        stack.append((a,[i,i]))
        continue

    while stack and stack[-1][0] != a:
        val,_ = stack.pop()
        st.remove(val)

    if not stack: raise AssertionError
    stack[-1][1][1] = i

for val,r in stack:
    print(*([val]*(r[1]-r[0]+1)),sep='\n')