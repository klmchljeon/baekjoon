n = int(input())
for _ in range(n):
    st = input()
    prev = None
    
    res = ''
    for i in st:
        if i != prev:
            res += i
            
        prev = i
        
    print(res)