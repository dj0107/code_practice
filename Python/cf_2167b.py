t = int(input())
for i in range(t):
    N = int(input())
    st = input()
    succ = 0
    best = 0
    for j in range(N):
        if st[j] == "0":
            succ += 1

        else:
            best = succ if succ > best else best
            succ = 0
        
    firstone = st.find("1")
    lastone = st.rfind("1")
    # 000100000100000 ->3,9, n=15...    
    circular = firstone + N - lastone - 1
    best = circular if circular > best else best

    print(best)