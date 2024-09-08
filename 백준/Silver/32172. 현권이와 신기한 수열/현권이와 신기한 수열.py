n = int(input())
st = set([0])

prev = 0
for i in range(1,n+1):
    ai = prev - i
    
    if ai < 0 or ai in st:
        ai = prev + i

    st.add(ai)
    prev = ai

print(prev)