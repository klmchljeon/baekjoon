#맞았는데 왜 틀리죠?
s1,s2 = map(int,input().split())
lst = []
for _ in range(s1+s2):
    a,b = input().split()
    lst.append(a==b)
    
for i in range(s1):
    if not lst[i]:
        print('Wrong Answer')
        exit()
        
for i in range(s2):
    if not lst[i]:
        print('Why Wrong!!!')
        exit()
        
print('Accepted')