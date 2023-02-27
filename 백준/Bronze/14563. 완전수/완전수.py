t = int(input())
d = list(map(int,input().split()))

for num in d:
    st = set()
    for i in range(2,int(num**0.5)+1):
        if num%i == 0:
            st.add(i)
            st.add(num//i)

    res = sum(st) + (num!=1)
    if res == num:
        print('Perfect')
    elif res < num:
        print('Deficient')
    else:
        print('Abundant')