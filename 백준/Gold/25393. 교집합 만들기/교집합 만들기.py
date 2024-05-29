import sys
input = sys.stdin.readline

n = int(input())
st = set()
left = dict()
right = dict()

for _ in range(n):
    l,r = map(int,input().split())
    st.add((l,r))
    
    if not l in left:
        left[l] = r
    else:
        left[l] = max(left[l],r)

    if not r in right:
        right[r] = l
    else:
        right[r] = min(right[r],l)

q = int(input())
for _ in range(q):
    l,r = map(int,input().split())
    if (l,r) in st:
        print(1)
    else:
        flag1 = l in left and r < left[l]
        flag2 = r in right and right[r] < l

        if flag1 and flag2:
            print(2)
        else:
            print(-1)