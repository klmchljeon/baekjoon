from collections import deque

def solution(cards1, cards2, goal):
    a = deque(cards1)
    b = deque(cards2)
    
    for i in goal:
        if a and a[0] == i:
            a.popleft()
            
        elif b and b[0] == i:
            b.popleft()
            
        else:
            return 'No'
    
    return 'Yes'