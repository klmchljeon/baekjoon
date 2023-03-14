def solution(elements):
    st = set()
    n = len(elements)
    for i in range(n):
        tmp = 0
        for j in range(i,i+n):
            tmp += elements[j%n]
            st.add(tmp)
    
    answer = len(st)
    return answer