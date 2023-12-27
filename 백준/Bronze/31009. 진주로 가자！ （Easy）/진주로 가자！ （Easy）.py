n = int(input())
d = []
cost = None
for i in range(n):
    st,c = input().split()
    c = int(c)
    if st == 'jinju':
        cost = c
  
    d.append(c)
    
cnt = 0
for i in d:
    cnt += cost<i
    
print(cost)
print(cnt)
        