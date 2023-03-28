#등장하지 않는 문자의 합
n = int(input())
for case in range(n):
    st = input()
    res = 0
    for i in range(26):
        alp = i+ord('A')
        if not chr(alp) in st:
            res += alp
            
    print(res)