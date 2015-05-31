while 1:
    t=float(input())
    sum=0.00
    n=1
    if t==0.00:
        break
    else:
        while t>=sum:
            sum+=1.00/(n+1.00)
            n+=1
    print n-1,"card(s)"
