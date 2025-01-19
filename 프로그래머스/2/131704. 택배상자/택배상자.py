def solution(order):
    answer = 0
    n = len(order)
    lst = order[::-1]
    
    stack = []
    for i in range(1,n+1):
        while stack and stack[-1] == lst[-1]:
            stack.pop()
            lst.pop()
            answer += 1
        
        if lst[-1] == i:
            lst.pop()
            answer += 1
            continue
            
        else:
            stack.append(i)
            
    while stack and stack[-1] == lst[-1]:
        stack.pop()
        lst.pop()
        answer += 1
    
    return answer