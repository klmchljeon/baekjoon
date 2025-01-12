def solution(elements):
    lst = [False]*1000001
    n = len(elements)
    for i in range(n):
        tmp = 0
        for j in range(i,i+n):
            tmp += elements[j%n]
            lst[tmp] = True
    
    answer = lst.count(True)
    return answer