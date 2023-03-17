from collections import deque

def solution(cards1, cards2, goal):
    a = deque(cards1)
    b = deque(cards2)
    
    n = len(goal)
    for i in range(n):
        if a and a[0] == goal[0]:
            a.popleft()
            goal.pop(0)
            
        elif b and b[0] == goal[0]:
            goal.pop(0)
            b.popleft()
            
        else:
            return 'No'
    
    return 'Yes'