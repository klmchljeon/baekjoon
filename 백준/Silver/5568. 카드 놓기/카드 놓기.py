def bt():
    if len(s) == k:
        tmp = ''
        for i in s:
            tmp += lst[i]

        st.add(tmp)
        return 
    
    for i in range(n):
        if not i in s:
            s.append(i)
            bt()
            s.pop()

    return 

n = int(input())
k = int(input())
lst = [input() for _ in range(n)]
st = set()

s = []
bt()

print(len(st))