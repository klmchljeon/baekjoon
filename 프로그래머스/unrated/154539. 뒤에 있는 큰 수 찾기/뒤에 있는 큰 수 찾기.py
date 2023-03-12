def solution(numbers):
    n = len(numbers)
    answer = [-1]*n
    
    stack = []
    for i in range(n):
        while stack and stack[-1][0] < numbers[i]:
            _,idx = stack.pop()
            answer[idx] = numbers[i]
        
        stack.append((numbers[i],i))
    
    return answer