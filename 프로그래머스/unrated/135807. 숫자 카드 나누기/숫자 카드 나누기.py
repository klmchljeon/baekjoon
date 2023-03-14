from math import gcd

def solution(arrayA, arrayB):
    answer = 0

    a = arrayA[0]
    for i in arrayA:
        a = gcd(a,i)
    
    flag = True
    for i in arrayB:
        flag &= bool(i%a)
        
    if flag:
        answer = a
    
    b = arrayB[0]
    for i in arrayB:
        b = gcd(b,i)
        
    flag = True
    for i in arrayA:
        flag &= bool(i%b)
        
    if flag:
        answer = max(answer,b)
    
    return answer