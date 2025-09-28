n = int(input())
for case in range(n):
    t = int(input())
    
    p = t%25
    if 0 <= p <= 16:
        print('ONLINE')
    else:
        print('OFFLINE')
