def judge1(lst):
    flag = True
    for i in range(len(lst)):
        if lst[i] != "dip":
            continue
        
        if 0 <= i-1 and lst[i-1] == "jiggle":
            continue
        
        if 0 <= i-2 and lst[i-2] == "jiggle":
            continue
        
        if i+1 < len(lst) and lst[i+1] == "twirl":
            continue
        
        lst[i] = "DIP"
        flag = False
    
    return flag

def judge2(lst):
    return lst[-3:] == ["clap","stomp","clap"]

def judge3(lst):
    if "twirl" in lst:
        return "hop" in lst
    
    return True

def judge4(lst):
    return lst[0] != "jiggle"

def judge5(lst):
    return "dip" in lst or "DIP" in lst

while True:
    try:
        lst = input().split()
    except:
        break
    
    flag = [0]*5
    for i in range(5):
        flag[i] = eval(f"judge{i+1}(lst)")
        
    error = []
    for i in range(5):
        if not flag[i]:
            error.append(i+1)
            
    print("form", end = ' ')
    if not error:
        print("ok:",end = ' ')
        
    elif len(error) == 1:
        print(f"error {error[0]}:", end = ' ')
        
    else:
        st = "errors " + ", ".join(["{}"]*(len(error)-1)) + " and {}:"
        print(st.format(*error), end = ' ')
        
    print(*lst,sep=' ')