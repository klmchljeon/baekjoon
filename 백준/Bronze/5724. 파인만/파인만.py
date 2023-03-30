while True:
    n = int(input())
    if not n: break
        
    res = 0
    for i in range(1,n+1):
        res += i**2
        
    print(res)