cnt = 0
def tmp(y,n,lst):
    global cnt
    if y == n:
        cnt += 1
        return

    for x in range(n):
        flag = True
        for j in range(y):
            if x == lst[j] or abs(x-lst[j]) == y-j:
                flag = False
                break

        if flag:
            lst[y] = x
            tmp(y+1,n,lst)
    return cnt

def solution(n):
    answer = 0
    lst = [0] * n
    answer = tmp(0,n,lst)
    
    return answer