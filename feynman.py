while 1:
    n=int(raw_input())
    if n==0:
        break
    else:
        total=0
        for i in range(1,n+1):
            total+=(i*i) 
        print total
