t=int(input())
for bam in range(t):
    num=int(input())
    x=2
    if num==1:
        print "TERM 1 IS 1/1"
        continue
    while True:
        s=(x*(x+1))/2
        shi=(((x-1)*x)/2)
        if num>shi and num<=s:
            break
        x=x+1
    
    if x%2==0:
        if num==s:
            print "TERM",num,"IS","%s/%s"%(x,1)
        elif num==shi+1:
            print "TERM",num,"IS","%s/%s"%(1,x)
        else:
            if (s-num)<=((s-shi-2)/2):
                print "TERM",num,"IS","%s/%s"%(x-(s-num),1+(s-num))
            else:
                print "TERM",num,"IS","%s/%s"%(1+(num-shi-1),x-(num-shi-1))
    else:
        if num==s:
            print "TERM",num,"IS","%s/%s"%(1,x)
        elif num==shi+1:
            print "TERM",num,"IS","%s/%s"%(x,1)
        else:
            if (s-num)==(num-shi-1):
                print "TERM",num,"IS","%s/%s"%((x+1)/2,(x+1)/2)
            elif (s-num)<=((s-shi-2)/2):
                print "TERM",num,"IS","%s/%s"%(x-(num-shi-1),1+(num-shi-1)) 
            else:
                print "TERM",num,"IS","%s/%s"%(1+(s-num),x-(s-num)) 
            
