st = input()
for i in st:
    s = 0
    for j in str(ord(i)):
        s += int(j)
    
    print(s*i)