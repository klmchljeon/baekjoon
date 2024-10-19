st = 'IK BDJK BDJK DIJK BDIJK BDIJK BDIJK BDIJK BDIJK DEIJK'
p = 'ABCDEFGHIJKLM'
lst = []
for i in st.split():
    lst.append(sorted(set(p)-set(i)))

n = int(input())
print(len(lst[n-1]))
print(*lst[n-1])