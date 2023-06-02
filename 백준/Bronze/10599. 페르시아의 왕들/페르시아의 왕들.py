while True:
    a,b,c,d = map(int,input().split())
    if not (a or b or c or d): break
        
    print(c-b,d-a)