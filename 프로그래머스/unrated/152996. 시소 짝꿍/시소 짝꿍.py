def solution(weights):
    weights.sort(reverse = True)
    answer = 0
    
    wei = [0]*2001
    for i in weights:
        answer += wei[i]
        answer += wei[i*2]
        if (i*3)%2 == 0:
            answer += wei[(i*3)//2]
        if (i*4)%3 == 0:
            answer += wei[(i*4)//3]
            
        wei[i] += 1
    
    return answer