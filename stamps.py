t=int(input())
c=1   
for x in range(t):
    n,m=raw_input().split(' ')
    n=int(n)
    m=int(m)
    sum=0
    su=0
    s=m-1
    count=0
    o=raw_input().split(' ')
    for y in range(m):
        o[y]=int(o[y])
        sum+=o[y]
    o.sort()
    if sum<n:
        print "Scenario #%s:"%(c)
        print "impossible"
        print ""
    else:
        while su<n:
            su+=o[s]
            count+=1
            s=s-1
        print "Scenario #%s:"%(c)
        print count
        print ""
    c=c+1	   	 	 	
