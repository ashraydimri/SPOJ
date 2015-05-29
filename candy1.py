while True:
    t=int(input())
    if t is -1:
        break
    
    total=0
    arr=[]
    out=0
    for x in range(t):
        n=int(input())
        total+=n
        arr.append(n)
    if total%t!=0:
        print -1
    else:
        avg=total/t
        for i in arr:
            temp=avg-i
            if temp>0:
                out+=temp
        print out
