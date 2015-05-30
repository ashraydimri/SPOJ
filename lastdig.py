t=int(input())
for x in range(t):
    a,b=raw_input().split(' ')
    a=int(a)
    b=int(b)
    ori=a%10
    arr=[a]
    if b==0:
        print 1
   
    else:
        a=a%10
        while ((a*ori)%10)!=ori:
        
            arr.append((a*ori)%10)
            a=(a*ori)%10
    
        print arr[(b-1)%len(arr)]%10
        
