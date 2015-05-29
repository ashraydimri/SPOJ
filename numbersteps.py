t=int(input())
for x in range(t):
    
    m,n = raw_input().split(' ')
    m=int(m)
    n=int(n)
    
    if m==n:
        if m%2==0 and n%2==0:
            print m+n
        else:
            print m+n-1
    elif n==(m-2):
        if m%2==0 and n%2==0:
            print m+n
        else:
            print (m-1)+n
    else:
        print "No number"
