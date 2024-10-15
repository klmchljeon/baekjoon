import sys

lst = sys.stdin.readlines()
for i in lst:
    st = i
    while "BUG" in st:
        st = st.replace("BUG","")

    print(st,end ='')